def test_data_path():
    from fig_remake.data_path import DATA

    data_labels = ['IgG', 'TAZ', 'TEAD4', 'YAP']
    for label in data_labels:
        assert DATA(label).exists()


def test_reference_path():
    d = 'G:/My Drive/BioData/GRCh38_noalt_as'
    from pathlib import Path

    assert Path(d).exists()
