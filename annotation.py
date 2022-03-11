from bs4 import BeautifulSoup
import yake
import urllib
import urllib.request
import sys


class annotation:

    def annotate(self, link, lang):

        req = urllib.request.Request(
            link, headers={'User-Agent': "Magic Browser"})
        usock = urllib.request.urlopen(req)
        page = usock.read()
        usock.close()

        soup = BeautifulSoup(page, 'html.parser')
        html_text = soup.get_text()
        text = html_text

        kw_extractor = yake.KeywordExtractor()
        language = lang
        max_ngram_size = 3
        deduplication_threshold = 0.9
        numOfKeywords = 10
        custom_kw_extractor = yake.KeywordExtractor(
            lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
        keywords = custom_kw_extractor.extract_keywords(text)

        joined_keywords = []
        for kw in keywords:
            joined_keywords.append(kw[0])

        max_ngram_size_1 = 3
        deduplication_threshold_1 = 0.9
        numOfKeywords_1 = 3
        custom_kw_extractor_1 = yake.KeywordExtractor(
            lan=language, n=max_ngram_size_1, dedupLim=deduplication_threshold_1, top=numOfKeywords_1, features=None)
        summary_of_keywords = custom_kw_extractor_1.extract_keywords(
            ' '.join(joined_keywords))

        result = [self.removeAppearancePercentage(
            sok) for sok in summary_of_keywords]

        return result

    def removeAppearancePercentage(self, el):
        return el[0]
