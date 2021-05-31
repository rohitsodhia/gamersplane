from enum import Enum
from typing import Dict

from django.core.cache import cache
from django.db import models


class CacheKeys(Enum):
    FORUM_DETAILS = "forum_details"
    FORUM_CHILDREN = "forum_children"
    GAME_DETAILS = "game_details"
    SYSTEM_DETAILS = "system_details"


CACHE_KEY_MAP = {
    "forum_details": "forum:{id}:details",
    "forum_children": "forum:{id}:children",
    "game_details": "game:{id}",
    "system_details": "system:{id}",
}


def generate_cache_id(cache_key: str, format_vars: Dict) -> str:
    key = CACHE_KEY_MAP[cache_key].format(**format_vars)
    return key


def get_objects_by_id(ids, model: models.Model, cache_key: str) -> models.Model:
    if type(ids) in [int, str]:
        obj = cache.get(generate_cache_id(cache_key, {"id": ids}))
        if not obj:
            obj = model.objects.get(id=ids)
            set_cache(cache_key, {"id": ids}, obj)
        else:
            cache.touch(CACHE_KEY_MAP[cache_key].format(id=ids))
        return obj

    cache_keys = [generate_cache_id(cache_key, {"id": id}) for id in ids]
    obj_caches = cache.get_many(cache_keys)
    objs = {val.id: val for _, val in obj_caches.items()}
    retrieved_objs = objs.keys()
    objs_to_get = list(set(ids) - set(retrieved_objs))
    if objs_to_get:
        model_objs = model.objects.filter(id__in=objs_to_get)
        for obj in model_objs:
            objs[obj.id] = obj
            obj_caches[generate_cache_id(cache_key, {"id": obj.id})] = obj
        cache.set_many(obj_caches)
    for key in retrieved_objs:
        cache.touch(key)
    return objs


def set_cache(key: str, format_vals: Dict, value) -> None:
    cache.set(generate_cache_id(key, format_vals), value)
