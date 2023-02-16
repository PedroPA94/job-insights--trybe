from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs = read(path)
    max_salary = {
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    }
    return max(max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    min_salary = {
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    }
    return min(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("Job salaries do not exist")

    validate_salaries(job["min_salary"], job["max_salary"], salary)

    return int(job["min_salary"]) <= int(salary) <= int(job["max_salary"])


def validate_salaries(
    min_salary: Union[int, str],
    max_salary: Union[int, str],
    salary: Union[int, str],
) -> None:
    salaries = [min_salary, max_salary, salary]

    int_or_str_salaries = [type(value) in (int, str) for value in salaries]

    valid_str_salaries = [
        value.isnumeric() for value in salaries if isinstance(value, str)
    ]

    if not all(int_or_str_salaries) or not all(valid_str_salaries):
        raise ValueError("Job salaries must be valid integers")

    if min_salary > max_salary:
        raise ValueError("Min salary can't be greater than max salary")


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
