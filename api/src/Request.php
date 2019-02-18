<?php

namespace App;

class Request extends \Slim\Http\Request
{

	public function has(string $param) {
		$postParams = $this->getParsedBody();
		$getParams = $this->getQueryParams();
		if (
			(is_array($postParams) && isset($postParams[$param])) ||
			(is_object($postParams) && property_exists($postParams, $param)) ||
			isset($getParams[$param])
		) {
			return true;
		}

		return false;
	}

	public function get(string $param, $default = null) {
		return $this->has($param) ? $this->getParam($param) : $default;
	}

}
