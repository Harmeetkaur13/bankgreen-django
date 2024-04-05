from brand.models import BrandFeature
from brand.models.commentary import InstitutionCredential, InstitutionType
from json import JSONEncoder


def get_institution_data():
    """
    Retrieve all Institute data from the database.
    """
    return InstitutionType.objects.all(), InstitutionCredential.objects.all()


def concat_brand_feature_data(brand_id):
    """
    Return concatenated brand feature data fieldwise.
    """
    data_dict = {}

    brand_feature_data = BrandFeature.objects.filter(brand_id=brand_id)

    if brand_feature_data:
        data_dict["brand_feature_id"] = ",".join([str(x.id) for x in brand_feature_data])
        data_dict["feature"] = ",".join([str(x.feature) for x in brand_feature_data])

    return data_dict


class PrettyJSONEncoder(JSONEncoder):
    def __init__(self, *args, indent, sort_keys, **kwargs):
        super().__init__(*args, indent=2, sort_keys=False, **kwargs)
