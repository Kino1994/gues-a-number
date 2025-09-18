# Guess a Number — Thirds vs Pure Binary Strategy

This project simulates two strategies for the classic “guess a number” game:

1. **Thirds → Binary Strategy**  
   - Split the range into **1/3 and 2/3**.  
   - Ask if the number is in the first third (`<= N/3`).  
   - Only if not, ask about the second threshold (`<= 2N/3`).  
   - Then apply **binary search** within the chosen third.

2. **Pure Binary Strategy**  
   - Always split the range in half.  
   - Continue dichotomically until the number is found.

We ran **1,000,000 simulations** for each range and strategy:  
- `1..100`  
- `1..1,000`  
- `1..10,000`  
- `1..100,000`  
- `1..1,000,000`  
- `1..10,000,000`  
- `1..100,000,000`  
- `1..1,000,000,000`

---

## Results Summary

| Range       | Strategy        | Mean  | Std  | Min | P50 | P90 | P99 | Max |
|-------------|-----------------|-------|------|-----|-----|-----|-----|-----|
| **1..100**      | Thirds→Binary | 6.75  | 0.55 | 6   | 7   | 7   | 8   | 8   |
|               | Pure Binary    | 6.72  | 0.45 | 6   | 7   | 7   | 7   | 7   |
| **1..1,000**    | Thirds→Binary | 10.13 | 0.69 | 9   | 10  | 11  | 11  | 11  |
|               | Pure Binary    | 9.98  | 0.15 | 9   | 10  | 10  | 10  | 10  |
| **1..10,000**   | Thirds→Binary | 13.44 | 0.63 | 12  | 14  | 14  | 14  | 14  |
|               | Pure Binary    | 13.36 | 0.48 | 13  | 13  | 14  | 14  | 14  |
| **1..100,000**  | Thirds→Binary | 16.70 | 0.50 | 16  | 17  | 17  | 18  | 18  |
|               | Pure Binary    | 16.69 | 0.46 | 16  | 17  | 17  | 17  | 17  |
| **1..1,000,000**| Thirds→Binary | 20.09 | 0.68 | 19  | 20  | 21  | 21  | 21  |
|               | Pure Binary    | 19.95 | 0.22 | 19  | 20  | 20  | 20  | 20  |
| **1..10,000,000**| Thirds→Binary| 23.41 | 0.64 | 22  | 23  | 24  | 24  | 24  |
|               | Pure Binary    | 23.32 | 0.47 | 23  | 23  | 24  | 24  | 24  |
| **1..100,000,000**| Thirds→Binary| 26.66 | 0.48 | 25  | 27  | 27  | 27  | 27  |
|               | Pure Binary    | 26.66 | 0.47 | 26  | 27  | 27  | 27  | 27  |
| **1..1,000,000,000**| Thirds→Binary| 30.06 | 0.68 | 29  | 30  | 31  | 31  | 31  |
|               | Pure Binary    | 29.93 | 0.26 | 29  | 30  | 30  | 30  | 30  |

---

## Full Decile Tables (P10…P100)

### Range 1..100
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 6   | 6   | 6   | 7   | 7   | 7   | 7   | 7   | 7   | 8    |
| Pure Binary     | 6   | 6   | 7   | 7   | 7   | 7   | 7   | 7   | 7   | 7    |

---

### Range 1..1,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 9   | 10  | 10  | 10  | 10  | 10  | 11  | 11  | 11  | 11   |
| Pure Binary     | 10  | 10  | 10  | 10  | 10  | 10  | 10  | 10  | 10  | 10   |

---

### Range 1..10,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 13  | 13  | 13  | 13  | 14  | 14  | 14  | 14  | 14  | 14   |
| Pure Binary     | 13  | 13  | 13  | 13  | 13  | 14  | 14  | 14  | 14  | 14   |

---

### Range 1..100,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 16  | 16  | 16  | 17  | 17  | 17  | 17  | 17  | 17  | 18   |
| Pure Binary     | 16  | 16  | 16  | 17  | 17  | 17  | 17  | 17  | 17  | 17   |

---

### Range 1..1,000,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 19  | 20  | 20  | 20  | 20  | 20  | 20  | 21  | 21  | 21   |
| Pure Binary     | 20  | 20  | 20  | 20  | 20  | 20  | 20  | 20  | 20  | 20   |

---

### Range 1..10,000,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 23  | 23  | 23  | 23  | 23  | 23  | 23  | 24  | 24  | 24   |
| Pure Binary     | 23  | 23  | 23  | 23  | 23  | 23  | 23  | 23  | 24  | 24   |

---

### Range 1..100,000,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 26  | 26  | 26  | 27  | 27  | 27  | 27  | 27  | 27  | 27   |
| Pure Binary     | 26  | 26  | 26  | 27  | 27  | 27  | 27  | 27  | 27  | 27   |

---

### Range 1..1,000,000,000
| Strategy        | P10 | P20 | P30 | P40 | P50 | P60 | P70 | P80 | P90 | P100 |
|-----------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| Thirds→Binary   | 29  | 30  | 30  | 30  | 30  | 30  | 30  | 30  | 31  | 31   |
| Pure Binary     | 30  | 30  | 30  | 30  | 30  | 30  | 30  | 30  | 30  | 30   |

---

## Interpretation

- **Pure Binary**  
  - Never exceeds ⌈log₂(N)⌉.  
  - More consistent across all ranges.  

- **Thirds → Binary**  
  - Gives a **1-step advantage at P10** in several ranges (100, 1k, 1M, 1B).  
  - But suffers a **1-step penalty in upper deciles** (P90–P100).  

👉 The **pattern repeats** as ranges grow:  
- Advantage at ~P10.  
- Disadvantage at ~P90+.  
- On average, Pure Binary is better.

---

## How to Run

```bash
python guess_game_large.py

