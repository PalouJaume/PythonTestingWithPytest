from subprocess import run

def test_sums():
    result = run(["python", "src/sums.py"],
                  capture_output=True, text=True)
    output = result.stdout
    assert output == "200.00\n"
