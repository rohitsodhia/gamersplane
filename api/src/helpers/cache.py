from enum import Enum

from django.core.cache import cache


class CacheKeys(Enum):
    FORUM_DETAILS = "forum_details"
    FORUM_CHILDREN = "forum_children"
    GAME_DETAILS = "game_details"


CACHE_KEY_MAP = {
    "forum_details": "forum:{id}:details",
    "forum_children": "forum:{id}:children",
    "game_details": "game:{id}",
}


def get_objects_by_id(ids, model, cache_key):
    if type(ids) in [int, str]:
        obj = cache.get(CACHE_KEY_MAP[cache_key].format(id=id))
        if not obj:
            obj = model.objects.get(id=ids)
            cache.set(CACHE_KEY_MAP[cache_key].format(id=id), obj)
        else:
            cache.touch(CACHE_KEY_MAP[cache_key].format(id=id))
        return obj

    cache_keys = [CACHE_KEY_MAP[cache_key].format(id=id) for id in ids]
    obj_caches = cache.get_many(cache_keys)
    objs = {val.id: val for _, val in obj_caches.items()}
    retrieved_objs = objs.keys()
    objs_to_get = list(set(ids) - set(retrieved_objs))
    if objs_to_get:
        model_objs = model.objects.filter(id__in=objs_to_get)
        for obj in model_objs:
            objs[obj.id] = obj
            obj_caches[CACHE_KEY_MAP[cache_key].format(id=obj.id)] = obj
        cache.set_many(obj_caches)
    for key in retrieved_objs:
        cache.touch(key)
    return objs
