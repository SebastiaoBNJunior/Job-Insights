from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",")
            for row in data:
                if row:
                    self.jobs_list.append(row)
        return self.jobs_list

    def printList(self):
        for job in self.jobs_list:
            try:
                print(job)
            except UnicodeEncodeError:
                print(job.encode('utf-8'))

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set(
            job['job_type'].strip()
            for job in self.jobs_list
            if 'job_type' in job
        )
        return list(unique_job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filter_criteria: Dict[str, str]
    ) -> List[Dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("Os filtros devem ser um dicionário")

        filtered_jobs = [
            job for job in jobs
            if all(job.get(key) == value for key, value in filter_criteria
                   .items())
        ]
        return filtered_jobs
