from enum import Enum, EnumMeta, unique

"""Metadata controlled vocabularies used in iRODS."""


def with_namespace(ns: str):
    """Returns a metaclass that may be used to add a property 'namespace' to
    an Enum. The metaclass is a subclass of EnumMeta in order to permit
    this.

    e.g.
       class MyEnum(Enum, metaclass=with_namespace("mynamespace")):
          X = "x"
          Y = "y"

       MyEnum.namespace == "mynamespace" is True


    This allows the namespace of the Enum to be accessed in the same
    syntactic style as the Enum members.
    """

    class WithNamespace(EnumMeta):
        """Metaclass adding a 'namespace' property an Enum"""

        @property
        def namespace(self):
            return ns

    return WithNamespace


@unique
class DublinCore(Enum, metaclass=with_namespace("dcterms")):
    """Dublin Core metadata"""

    AUDIENCE = "audience"
    CREATED = "created"
    CREATOR = "creator"
    IDENTIFIER = "identifier"
    MODIFIED = "modified"
    PUBLISHER = "publisher"
    TITLE = "title"


@unique
class SampleMetadata(Enum):
    """SequenceScape Sample metadata."""

    SAMPLE_ACCESSION_NUMBER = "sample_accession_number"
    SAMPLE_COHORT = "sample_cohort"
    SAMPLE_COMMON_NAME = "sample_common_name"
    SAMPLE_CONSENT = "sample_consent"
    SAMPLE_CONSENT_WITHDRAWN = "sample_consent_withdrawn"
    SAMPLE_CONTROL = "sample_control"
    SAMPLE_DONOR_ID = "sample_donor_id"
    SAMPLE_ID = "sample_id"
    SAMPLE_NAME = "sample"
    SAMPLE_PUBLIC_NAME = "sample_public_name"
    SAMPLE_SUPPLIER_NAME = "sample_supplier_name"


@unique
class StudyMetadata(Enum):
    """SequenceScape Study metadata."""

    STUDY_ACCESSION_NUMBER = "study_accession_number"
    STUDY_ID = "study_id"
    STUDY_NAME = "study"
    STUDY_TITLE = "study_title"


@unique
class ONTMetadata(Enum, metaclass=with_namespace("ont")):
    """Oxford Nanopore platform metadata"""

    EXPERIMENT_NAME = "experiment_name"
    INSTRUMENT_SLOT = "instrument_slot"
