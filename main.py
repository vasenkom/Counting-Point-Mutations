def func(DNA1, DNA2):
  count = 0
  
  for x, y in zip(DNA1, DNA2):
    if x != y:
      count = count + 1
  print("Number of mutations: ", count)

#Insert your sequences to compare. The sequences are left for example
DNA1 = "CCCAACCCGTTAGCTTGGTGGAGGGCCAAGCGTAATACCAGAGCTCAGAGACCACAGTATGTCATTCCAGTGCAATTCAGTCGATGCAGCAGGCTGGGGTTCGCTGTTACGCCAAAAAAGCTCGGCTCAATATAGAGCAGAAGTCTAATGTCCACACACTAGGGGTGGCACGGCGTGATGCTAGATTTAGATCAATACTACCCGAATTAGGTCGTTGGCTCCCGGCCAGGTACAAGCATATATGAACCATGTAGCGGCGGCGCAGTCTTCGAATCTCACGGGAGGACGCTACTGCCCTTCTCCCTGTGTTGAGAAAGGGGCTGTTGGAAACTGCAGACTTTTGGGTGTCAATGTGAAATCTTTTACAGCCAGTGTCTACCTCCTAAGAAGTCGGTGTCTTTGCGGCCAATATCTCGATCGTCCATGACTACGCGTTGTGTTACTTGGGGGTATCCAAAGCTTCGAGACGGATAGCCGATTCATGCTGTATACCCCAGTTGATTGCGCTGCAATCAAAGTGCTTTTCACAACCAGATCTGGCGGTATTTTCCCGAACTATAGGTGGGCTGACACGGGGAGACACATTAGATTGAAAACACGCTCATGACATCATGAGTGCAAGCTAACCGTTGTTTAGGTACACCATGGGTCTTCACGCCTATGTGCGCTTGCACATGATGATCCCAATTTAAGGCGACGGCGCGGAAACAAACGGTTGTAAGACCGGGGGGTTTCAACTTTGGTCTTCTCAAGCCTGCTGTTGGGGCCGGACTAACAAGGGTCTTCATCACTGCGAGAGGCGCACTGGAGTATAATTGCATCAACGACCATTGCGAGCCCCAGTTCCTCTCCGAGGCTAGCGAGTTGTGCCTTAAAACTCGGTTTGGGTCTAGACGTAGTCACTCCGCTTGTTAGCCCCATGGTGATGCCTTTGGCCAATCCTGCCGAGCACGATTTTCTAGAGCACGGACTTCTTCTTGTTAATGCCCACGGAGCCAGT"
DNA2 = "CGCATCCCCTGACCTTAGTTGTCGGACAAGTTAAATCCTCAAGGTCAGAGAACTCATTTTTGAACCCTCGATCTATTAGGACGATGTGGCGCTGGCTCTCCCGGAGAGACTGCCAGTGGGATTGCATAAATCCCGCCAAGTAGTCCAAGTTCTCCGCGGCAGCGTTGCCACGGTTTTACCGGGCTGTGAGATCAATATTATCCCGTTTACGGCGTTGGGTTTCAAGATAGAACGAGCAGAGTCGAATGCTTTAGTTAGGGGACTATCTTCGAACGATCAACCAACACAGTAGTTGTGGGCTCCCGGGCAGAATAGATATGCGGGTCAAAACGGCAGGATTGTGGGCACCAATGCGAAATCCTTTAGGCTGGCTGTCTCTGTTCTAAGTAGCCCCTGGCTTAGGGTCCCGCGTCTCGTCGGCCCATACGGATCCGTAGTGGTATTACAAGGTAGCCAATCGGTAGAGACTGATCGCGGATCTAAGCTGGTCCCGGAAGGTCTTTGCGTTGAAGTCCAGATGCGTCCCATCCGCAGGTTTTGTGGATTTTTCTGTAGCATAAGATGCATTCACCTGGGGAGCGCCATTCGATGGACCCGGCGCTCCAACGATGATCAGGGCAAGCTATACGTTGTCACGCTACATAATAGGACGGTACGCTTATCGACGTTTGCACATGAATATCATTAGTCCGATGAAACTCACTGAAACTGACTGTTGGAAGACTGGTTGATTCCAACTACGATAGTCGAAAGCCTCCCGCCCCTCCGCGACTCACTAGCGGATGGACCTGTGCGAACGACCCGCTTTGTTGCAACAACAACCCTAAACATTGCGAACGCGAATAGCTCTACTTGCTGAGTGAGCTGTACTCGAATAGTCGCACGCGGCCCTTACTATCGGTCGACCCTATTAGGTGCGAGCGTGTTTGAGTAGTCGACGTCGGCTGGGTACTTTACTCTTAGGCATTGAATTGGTTTGGCGCCAGACCTAACACCCACA"

func(DNA1, DNA2)