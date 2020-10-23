import Bio
from Bio import SeqIO
from dnachisel import *

finalSequence=list()

HumanInsulinFASTA=list(SeqIO.parse("Genome/Human Insulin.fasta","fasta"))
for record in HumanInsulinFASTA:
    print(record.description)
    print(record.seq)
    strSeq=str(record.seq)[:(len(str(record.seq))//3)*3]
    problem = DnaOptimizationProblem(
        sequence=strSeq,
        constraints=[
            EnforceTranslation()
        ],
        objectives=[CodonOptimize(species=34199)]
    )

    # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE

    problem.resolve_constraints()
    problem.optimize()

    # PRINT SUMMARIES TO CHECK THAT CONSTRAINTS PASS

    print(problem.constraints_text_summary())
    print(problem.objectives_text_summary())

    # GET THE FINAL SEQUENCE (AS STRING OR ANNOTATED BIOPYTHON RECORDS)

    final_sequence = problem.sequence  # string
    final_sequence = Bio.SeqRecord.SeqRecord(
        Bio.Seq.Seq(final_sequence),
        id=record.id,
        name=record.name,
        description=record.description+" Optimized for Aloe vera based on Kazusa species 34199."
    )
    #final_record = problem.to_record(with_sequence_edits=True)
    finalSequence.append(final_sequence)

for newRecord in finalSequence:
    print(newRecord.description)
    print(newRecord.seq)