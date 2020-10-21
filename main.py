import Bio
from Bio import SeqIO
from Bio import AlignIO

"""
# Test
AloeChloroplastGenBank=AlignIO.read("AloeChloroplast.gb","genbank")
tmpFile=open(".tmp/tempAloeChloroplastAllignmentFile.txt","w")
for record in AloeChloroplastGenBank:
    print(record.id)
    tmpFile.write(str(record.seq))
tmpFile.close()
"""

"""
AloeChloroplastGenBank=list(SeqIO.parse("AloeChloroplast.gb","genbank"))
for record in AloeChloroplastGenBank:
    print(record.id)
    print(repr(record.seq))
    print(len(record.seq))
"""

# Load sequence
AloeChloroplastGenBank=SeqIO.read("AloeChloroplast.gb","genbank")
print(AloeChloroplastGenBank.id)