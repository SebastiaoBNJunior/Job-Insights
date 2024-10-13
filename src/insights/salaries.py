from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        max_salaries = [int(job['max_salary'].strip()) for job in self
                        .jobs_list if job.get('max_salary', '')
                        .strip().isdigit()]
        return max(max_salaries) if max_salaries else 0

    def get_min_salary(self) -> int:
        min_salaries = [int(job['min_salary'].strip()) for job in self
                        .jobs_list if job.get('min_salary', '')
                        .strip().isdigit()]
        return min(min_salaries) if min_salaries else 0

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if (
            "max_salary" not in job
            or "min_salary" not in job
            or not str(job["max_salary"]).strip().isdigit()
            or not str(job["min_salary"]).strip().isdigit()
        ):
            raise ValueError

        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError

        if not isinstance(salary, int) and (
            not isinstance(salary, str) or not salary.strip().isdigit()
        ):
            raise ValueError

        return min_salary <= int(salary) <= max_salary

    def filter_by_salary_range(
        self, jobs: List[Dict], salary: Union[str, int]
    ) -> List[Dict]:
        return [job for job in jobs if self.matches_salary_range(job, salary)]
