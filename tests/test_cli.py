from ballard_weather_service import cli

def test_cli_template():
    assert cli.cli() is None
