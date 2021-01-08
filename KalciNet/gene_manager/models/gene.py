from django.db import models
from jsonfield import JSONField

class gene(models.Model):
    """
    """

    ## attribute
    symbol = models.TextField(default="NA")
    name = models.TextField(default="NA")
    ensembl_id = models.TextField(default="NA")
    entrez_id = models.TextField(default="NA")
    hgnc_id = models.TextField(default="NA")
    alias_list = JSONField(default=[])
    alternative_name_list = JSONField(default=[])
    description = models.TextField(default="NA")
    localisation = models.TextField(default="NA")
    gene_type = models.TextField(default="NA")
    pmid_list = JSONField(default=[])
    pathway_list = JSONField(default=[])
    gene_card_link = models.TextField(default="NA")
    ensembl_link = models.TextField(default="NA")
