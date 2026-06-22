import re
import time
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor

POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}

def sentiment_score(text: str) -> int:
    """CPU-bound: tokenizuj, policz pozytywne minus negatywne."""
    # Zadanie 2.1: zaimplementuj
    # 1. lowercase, regex \w+ -> lista slow
    text = text[0]
    words = re.findall(r"\w+", text.lower())
    # 2. zliczyc ile slow w POS_WORDS, ile w NEG_WORDS
    # 3. zwrocic roznice
    return sum(w in POS_WORDS for w in words) - sum(w in NEG_WORDS for w in words)



def run_benchmark(texts):
    # czas sekwencyjny [s.score(t) for t in texts]
    t0 = time.time()
    seq_results = [sentiment_score(t) for t in texts]
    seq_time = time.time() - t0
    print(f"Sekwencyjnie (5000 probek): {seq_time:.2f}s")

    # czas ThreadPool (max_workers=16)
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=16) as pool:
        thread_results = list(pool.map(sentiment_score, texts))
    thread_time = time.time() - t0

    print(f"ThreadPool: {thread_time:.2f}s | {seq_time/thread_time:.1f}x")

    # czas multiprocessing.Pool (procesy = os.cpu_count())
    t0 = time.time()

    with Pool(processes=cpu_count()) as pool:
        mp_results = pool.map(sentiment_score, texts, chunksize=100)

    mp_time = time.time() - t0

    print(f"Multiprocessing: {mp_time:.2f}s | {seq_time/mp_time:.1f}x")

    # bar plot 3 czasow
    labels = ["sequential", "threads", "multiprocessing"]
    times = [seq_time, thread_time, mp_time]

    plt.bar(labels, times)
    plt.ylabel("Czas (sek)")
    plt.title("Porównanie czasów multiprocessingu")
    plt.show()

    return seq_time, thread_time, mp_time
