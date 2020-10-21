import Bio
from Bio import SeqIO

"""
AloeChloroplastGenBank=list(SeqIO.parse("AloeChloroplast.gb","genbank"))
for record in AloeChloroplastGenBank:
    print(record.id)
    print(repr(record.seq))
    print(len(record.seq))
"""

# Load genbank file.
AloeChloroplastGenBank=SeqIO.read("AloeChloroplast.gb","genbank")
print(AloeChloroplastGenBank.id)