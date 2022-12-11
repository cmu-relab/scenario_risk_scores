# coding=utf-8
# Lint as: python3
"""Scenario annotation data without categories."""

import os

import datasets

import sys
sys.path.insert(1, 'D:\GradProject\mobile_privacy\mobile_privacy')
from notebooks.lib_analysis import *


logger = datasets.logging.get_logger(__name__)


_CITATION = """TBD"""

_DESCRIPTION = """TBD"""

_URL = "https://data.deepai.org/conll2003.zip"
_TRAINING_FILE = "train.txt"
_DEV_FILE = "valid.txt"
_TEST_FILE = "test.txt"


class Conll2003Config(datasets.BuilderConfig):
    """BuilderConfig for scenario data."""

    def __init__(self, **kwargs):
        """BuilderConfig for scenario data.

        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(Conll2003Config, self).__init__(**kwargs)


class Conll2003(datasets.GeneratorBasedBuilder):
    """Conll2003 dataset."""

    BUILDER_CONFIGS = [
        Conll2003Config(name="scenarios", version=datasets.Version("1.0.0"), description="Scenario annotation dataset"),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "o",
                                "b-i",
                                "i-i",
                            ]
                        )
                    ),
                    # "pos_tags": datasets.Sequence(
                    #     datasets.features.ClassLabel(
                    #         names=[
                    #             '"',
                    #             "''",
                    #             "#",
                    #             "$",
                    #             "(",
                    #             ")",
                    #             ",",
                    #             ".",
                    #             ":",
                    #             "``",
                    #             "CC",
                    #             "CD",
                    #             "DT",
                    #             "EX",
                    #             "FW",
                    #             "IN",
                    #             "JJ",
                    #             "JJR",
                    #             "JJS",
                    #             "LS",
                    #             "MD",
                    #             "NN",
                    #             "NNP",
                    #             "NNPS",
                    #             "NNS",
                    #             "NN|SYM",
                    #             "PDT",
                    #             "POS",
                    #             "PRP",
                    #             "PRP$",
                    #             "RB",
                    #             "RBR",
                    #             "RBS",
                    #             "RP",
                    #             "SYM",
                    #             "TO",
                    #             "UH",
                    #             "VB",
                    #             "VBD",
                    #             "VBG",
                    #             "VBN",
                    #             "VBP",
                    #             "VBZ",
                    #             "WDT",
                    #             "WP",
                    #             "WP$",
                    #             "WRB",
                    #         ]
                    #     )
                    # ),
                    # "chunk_tags": datasets.Sequence(
                    #     datasets.features.ClassLabel(
                    #         names=[
                    #             "O",
                    #             "B-ADJP",
                    #             "I-ADJP",
                    #             "B-ADVP",
                    #             "I-ADVP",
                    #             "B-CONJP",
                    #             "I-CONJP",
                    #             "B-INTJ",
                    #             "I-INTJ",
                    #             "B-LST",
                    #             "I-LST",
                    #             "B-NP",
                    #             "I-NP",
                    #             "B-PP",
                    #             "I-PP",
                    #             "B-PRT",
                    #             "I-PRT",
                    #             "B-SBAR",
                    #             "I-SBAR",
                    #             "B-UCP",
                    #             "I-UCP",
                    #             "B-VP",
                    #             "I-VP",
                    #         ]
                    #     )
                    # ),
                }
            ),
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        downloaded_file = dl_manager.download_and_extract(_URL)
        data_files = {
            "train": os.path.join(downloaded_file, _TRAINING_FILE),
            "dev": os.path.join(downloaded_file, _DEV_FILE),
            "test": os.path.join(downloaded_file, _TEST_FILE),
        }

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": data_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": data_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            tokens = []
            pos_tags = []
            chunk_tags = []
            ner_tags = []
            for line in f:
                if line.startswith("-DOCSTART-") or line == "" or line == "\n":
                    if tokens:
                        yield guid, {
                            "id": str(guid),
                            "tokens": tokens,
                            "pos_tags": pos_tags,
                            "chunk_tags": chunk_tags,
                            "ner_tags": ner_tags,
                        }
                        guid += 1
                        tokens = []
                        pos_tags = []
                        chunk_tags = []
                        ner_tags = []
                else:
                    # conll2003 tokens are space separated
                    splits = line.split(" ")
                    tokens.append(splits[0])
                    pos_tags.append(splits[1])
                    chunk_tags.append(splits[2])
                    ner_tags.append(splits[3].rstrip())
            # last example
            if tokens:
                yield guid, {
                    "id": str(guid),
                    "tokens": tokens,
                    "pos_tags": pos_tags,
                    "chunk_tags": chunk_tags,
                    "ner_tags": ner_tags,
                }