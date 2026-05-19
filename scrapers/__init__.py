"""
Scraper registry — add new scrapers here to make them auto-discoverable.
"""
from scrapers.base import BaseScraper, ScrapedJob
from scrapers.efinancialcareers import EFinancialCareersScraper
from scrapers.indeed_ch import IndeedChScraper
from scrapers.jobscout24 import JobScout24Scraper
from scrapers.jobs_ch import JobsChScraper
from scrapers.jobup_ch import JobupChScraper
from scrapers.linkedin_rss import LinkedInRssScraper
from scrapers.michael_page import MichaelPageScraper
from scrapers.swissdevjobs import SwissDevJobsScraper
from scrapers.zuri_jobs import ZuriJobsScraper

# Map source name → scraper class
SCRAPER_REGISTRY: dict[str, type[BaseScraper]] = {
    "jobs.ch": JobsChScraper,
    "jobscout24.ch": JobScout24Scraper,
    "swissdevjobs.ch": SwissDevJobsScraper,
    "indeed.ch": IndeedChScraper,
    "jobup.ch": JobupChScraper,
    "züri.jobs": ZuriJobsScraper,
    "efinancialcareers.ch": EFinancialCareersScraper,
    "linkedin.com": LinkedInRssScraper,
    "michael-page.ch": MichaelPageScraper,
}

ALL_SOURCES = list(SCRAPER_REGISTRY.keys())

__all__ = [
    "BaseScraper", "ScrapedJob", "SCRAPER_REGISTRY", "ALL_SOURCES",
    "JobsChScraper", "JobScout24Scraper", "SwissDevJobsScraper", "IndeedChScraper",
    "JobupChScraper", "ZuriJobsScraper", "EFinancialCareersScraper",
    "LinkedInRssScraper", "MichaelPageScraper",
]
