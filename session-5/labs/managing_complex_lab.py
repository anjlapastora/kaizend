class ScrapingJob(object):
    def __init__(self, name):
        self.name = name
        self.url = "<none>"
        self.selector = "<none>"
        self.save_file = "<none>"

    def load(self, url):
        self.url = url
        return self

    def find(self, selector):
        self.selector = selector
        return self

    def save(self, save_file):
        self.save_file = save_file
        return self


    def complete(self):
        print(f"[START] {self.name}")
        print(f"[URL] =  {self.url}")
        print(f"SELECTOR =  {self.selector}")
        print(f"SAVE_FILE =  {self.save_file}")
        print(f"[END] =  {self.name}")


def main():
    job = ScrapingJob("Job 1")
    job.load("<url>").find("target").save("<filename>").complete()

    job = ScrapingJob("Job 2")
    job.load("<url>").find("target").complete()
    
    job = ScrapingJob("Job 2")
    job.load("<url>").complete()


if __name__ == "__main__":
    main()




    


