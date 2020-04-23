# from src import office31
from office31 import office31


def test_intersection():
    train, val, test = office31("dslr", "webcam", image_resize=None, group_in_out=True)

    assert not set.intersection(set(train), set(val))
    assert not set.intersection(set(val), set(test))
    assert not set.intersection(set(test), set(train))


def test_resize():
    train, val, test = office31(
        "webcam", "amazon", image_resize=(240, 240), group_in_out=False
    )

    assert train.shape == ((240, 240, 3), (240, 240, 3), (), ())
    assert val.shape == ((240, 240, 3), (240, 240, 3), (), ())
    assert test.shape == ((240, 240, 3), (240, 240, 3), (), ())
