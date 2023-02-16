from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = 'tests/mocks/brazilians_jobs.csv'
    result_dict = read_brazilian_file(path)
    assert 'titulo' not in result_dict[0]
    assert 'salario' not in result_dict[0]
    assert 'tipo' not in result_dict[0]
    assert 'title' in result_dict[0]
    assert 'salary' in result_dict[0]
    assert 'type' in result_dict[0]
