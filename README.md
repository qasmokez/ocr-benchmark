# OCR Benchmark
Experimenting with popular OCR tools, with apple-ocr as the reference for performance. The `ipynb` includes dataset parsing and handler functions for the following OCR tools, checking each of their outputs and runtimes against the data.

### Models
- apple-ocr [docs](https://developer.apple.com/documentation/vision/) [wrapper1](https://github.com/louisbrulenaudet/apple-ocr/tree/main) [wrapper2](https://github.com/straussmaximilian/ocrmac/tree/main)
- Easy-OCR [repo](https://github.com/JaidedAI/EasyOCR)
- (In Progress) pytesseract [pip](https://pypi.org/project/pytesseract/) [tesseract](https://github.com/tesseract-ocr/tesseract)
- (TODO) Idefics2 [article](https://huggingface.co/blog/idefics2)


### Dataset
```
https://huggingface.co/datasets/getomni-ai/ocr-benchmark
```

### Benchmark
```
https://github.com/getomni-ai/benchmark
```

### Findings (In Progress)
Example benchmark output so far:
```
=========== apple-ocr ===========
Setup Time: 3.314018249511719e-05
Runtime: 0.6097888946533203
---- Output ----
0            Staff Shift Schedule
1    Fort Bradlv Medical Center -
2      Week of September 27, 2025
3                        Employee
4                Courtney Lebsack
5                     Linda Lesch
6                   Roberto Stehr
7                Horace Gleichner
8                    Stella Fadel
9                Jared Leannon II
Name: text, dtype: object

=========== easy-ocr ===========
Setup Time: 2.3394429683685303
Runtime: 6.487469911575317
---- Output ----
0          Staff Shift Schedule
1                          Fort
2         Bradly Medical Center
3    Week of September 27, 2025
4                      Employee
...
8                        Sun 28
9                        Mon 29
Name: text, dtype: object
```

### Notes (to self)
Tools:
- Benchmark
    - (https://getomni.ai/ocr-benchmark)
    - (https://github.com/getomni-ai/benchmark)
- Roboflow
    - (https://roboflow.com/)