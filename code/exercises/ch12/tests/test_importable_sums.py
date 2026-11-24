import sums

def test_main(capsys):
    sums.main()
    output = capsys.readouterr().out
    assert output == "200.00\n"