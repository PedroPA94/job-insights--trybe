from src.pre_built.sorting import sort_by
import pytest


jobs = [
        {"min_salary": 100, "max_salary": 300, "date_posted": "2020-07-08"},
        {"min_salary": 500, "max_salary": 900, "date_posted": "2021-07-08"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-07-08"},
        {"min_salary": 200, "max_salary": 0, "date_posted": "2023-01-01"},
    ]


def test_sort_by_criteria():

    min_salary_sort = [
        {"min_salary": 100, "max_salary": 300, "date_posted": "2020-07-08"},
        {"min_salary": 200, "max_salary": 0, "date_posted": "2023-01-01"},
        {"min_salary": 500, "max_salary": 900, "date_posted": "2021-07-08"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-07-08"},
    ]

    max_salary_sort = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-07-08"},
        {"min_salary": 500, "max_salary": 900, "date_posted": "2021-07-08"},
        {"min_salary": 100, "max_salary": 300, "date_posted": "2020-07-08"},
        {"min_salary": 200, "max_salary": 0, "date_posted": "2023-01-01"},
    ]

    date_sort = [
        {"min_salary": 200, "max_salary": 0, "date_posted": "2023-01-01"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-07-08"},
        {"min_salary": 500, "max_salary": 900, "date_posted": "2021-07-08"},
        {"min_salary": 100, "max_salary": 300, "date_posted": "2020-07-08"},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == min_salary_sort

    sort_by(jobs, 'max_salary')
    assert jobs == max_salary_sort

    sort_by(jobs, 'date_posted')
    assert jobs == date_sort

    with pytest.raises(ValueError, match='invalid sorting criteria'):
        sort_by(jobs, 'title')
