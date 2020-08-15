from contextlib import contextmanager


class Job: 
    def __init__(self, target_url=None, selector=None, save_file=None):
        self.target_url = target_url
        self.selector = selector
        self.save_file = save_file



@contextmanager
def scrapint_job(label):
    print(f"START {label}")
    job = Job()
    yield job
    print(f"TARGET_URL {job.target_url}")
    print(f"SELECTOR {job.selector}")
    print(f"SAVE FILE {job.save_file}")
    print(f"END {label}")

@contextmanager
def scraping_job_custom(label):
    print(f"START2 {label}")
    job = Job()
    yield job
    print(f"TARGET_URL2 {job.target_url}")
    print(f"SELECTOR2 {job.selector}")
    print(f"SAVE FILE2 {job.save_file}")
    print(f"END2 {label}")



def main():
    with scrapint_job("JOB 1") as job:
        job.target_url = "<url>"
        job.selector = "<selector>"
        job.save_file = "<filename>"

    with scrapint_job("JOB 2") as job:
        job.target_url = "<url 2>"
        job.selector = "<selector 2>"
        job.save_file = "<filename 2>"

    with scraping_job_custom("JOB 3") as job:
        job.target_url = "<url 3>"
        job.selector = "<selector 3>"
        job.save_file = "<filename 3>"

if __name__ == "__main__":
    main()