from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Termid:
    label: str
    type: str
    ilx: str
    definition: str
    id: int
    cid: int


@dataclass
class Fields:
    termid: Termid
    id: int
    position: int
    multi: int
    dataset_fields_template_id: int
    name: str
    required: int
    queryable: int


@dataclass
class Template:
    id: int
    uid: int
    labid: int
    active: int
    submitted: int
    timestamp: int
    name: str
    parent_id: int
    fields: List[Fields]


@dataclass
class DatasetInfo:
    name: str
    description: str
    uid: int
    timestamp: int
    lab_status: str
    curation_status: Optional[str]
    field_set: str
    active: int
    last_uploaded_time: int
    long_name: str
    id: int
    publications: str
    dataset_fields_template_id: int
    editor_status: Optional[str]
    record_count: int
    last_updated_time: int
    template: Template
