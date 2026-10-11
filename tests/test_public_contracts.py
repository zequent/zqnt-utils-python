import importlib
import pkgutil

import zqnt_utils.generated
from zqnt_api.generated.zqnt.common.v3 import common_pb2
from zqnt_utils.generated.zqnt.asset.v3 import asset_pb2


def _generated_modules() -> set[str]:
    return {
        module.name
        for module in pkgutil.walk_packages(
            zqnt_utils.generated.__path__, "zqnt_utils.generated."
        )
    }


def test_internal_messages_take_the_public_types_of_zqnt_api():
    request = asset_pb2.GetAssetRequest(asset=common_pb2.AssetRef(sn="SN-1"))

    assert request.asset.sn == "SN-1"
    assert common_pb2.DESCRIPTOR in asset_pb2.DESCRIPTOR.dependencies


def test_every_internal_module_imports():
    for name in _generated_modules():
        importlib.import_module(name)


def test_no_public_contract_is_generated_here():
    names = _generated_modules()

    assert "zqnt_utils.generated.zqnt.common_pb2" not in names
    assert "zqnt_utils.generated.zqnt.common.v3.common_pb2" not in names
