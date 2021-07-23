from typing import Any, Dict, List, Optional, Sequence, Type

from rest_framework.fields import Field
from rest_framework.pagination import BasePagination
from rest_framework.request import Request
from rest_framework.serializers import BaseSerializer
from typing_extensions import TypedDict

from .generators import BaseSchemaGenerator as BaseSchemaGenerator
from .inspectors import ViewInspector as ViewInspector

# OpenAPI requires its own typings. Below are minimal typing.
# TODO: evaluate using a 3rd party typing package for this, e.g.: https://github.com/meeshkan/openapi-typed

class DRFOpenAPIInfo(TypedDict, total=False):
    title: str
    version: str
    description: str

class externalDocumentationObject(TypedDict):
    description: str
    url: str

class DRFOpenAPISchema(TypedDict, total=False):
    openapi: str
    info: DRFOpenAPIInfo
    paths: Dict[str, Dict[str, Any]]
    components: Dict[str, Dict[str, Any]]
    security: List[Dict[str, List[Any]]]
    tags: List[Dict[str, Any]]
    externalDocs: externalDocumentationObject
    servers: List[Dict[str, Any]]

class SchemaGenerator(BaseSchemaGenerator):
    def get_info(self) -> DRFOpenAPIInfo: ...
    def check_duplicate_operation_id(self, paths: Dict[str, Dict[str, Any]]) -> None: ...
    def get_schema(self, request: Request = ..., public: bool = ...) -> DRFOpenAPISchema: ...  # type: ignore[override]

class AutoSchema(ViewInspector):
    operation_id_base: Optional[str] = ...
    component_name: Optional[str] = ...
    request_media_types: List[str] = ...
    response_media_types: List[str] = ...
    method_mapping: Dict[str, str] = ...
    def __init__(
        self, tags: Sequence[str] = ..., operation_id_base: Optional[str] = ..., component_name: Optional[str] = ...
    ) -> None: ...
    def get_operation(self, path: str, method: str) -> Dict[str, Any]: ...
    def get_component_name(self, serializer: BaseSerializer) -> str: ...
    def get_components(self, path: str, method: str) -> Dict[str, Any]: ...
    def get_operation_id_base(self, path: str, method: str, action: Any) -> str: ...
    def get_operation_id(self, path: str, method: str) -> str: ...
    def get_path_parameters(self, path: str, method: str) -> List[Dict[str, Any]]: ...
    def get_filter_parameters(self, path: str, method: str) -> List[Dict[str, Any]]: ...
    def allows_filters(self, path: str, method: str) -> bool: ...
    def get_pagination_parameters(self, path: str, method: str) -> List[Dict[str, Any]]: ...
    def map_choicefield(self, field: Field) -> Dict[str, Any]: ...
    def map_field(self, field: Field) -> Dict[str, Any]: ...
    def map_serializer(self, serializer: BaseSerializer) -> Dict[str, Any]: ...
    def map_field_validators(self, field: Any, schema: Any) -> None: ...
    def get_paginator(self) -> Optional[Type[BasePagination]]: ...
    def map_parsers(self, path: str, method: str) -> List[str]: ...
    def map_renderers(self, path: str, method: str) -> List[str]: ...
    def get_serializer(self, path: str, method: str) -> Optional[BaseSerializer]: ...
    def get_request_body(self, path: str, method: str) -> Dict[str, Any]: ...
    def get_responses(self, path: str, method: str) -> Dict[str, Any]: ...
    def get_tags(self, path: str, method: str) -> List[str]: ...
