"""Типичные примеры O-нотации (сложности алгоритмов)"""

"""     О(1) — в этом случае у нас нет числа n, как нет и зависимости от количества элементов.
               Такая оценка может быть, например, у алгоритмов, которые выполняют действие над одним элементом,
               допустим извлекают одну букву из строки. В строке может быть миллиард букв,
               а может быть десять, но первую букву мы всегда сможем извлечь за одно действие.
        О(log n) — log может пугать, но достаточно просто запомнить, что эта оценка быстрее линейной зависимости.
                   Если при линейной зависимости на 128 элементов мы потратим 128 действий, то при O(log n):
                   log 128 = 7 — нам понадобится всего семь действий.
                   Количество действий будет расти с количеством элементов, но происходить это будет гораздо медленнее.
        O(n) — линейная оценка, самая простая (но не самая эффективная, как мы видели ранее).
               Сколько элементов — столько и действий.
        О(n * log n) — пожалуй, самая длинная из вариантов, она говорит о том, что алгоритм работает медленнее,
               чем при линейной оценке. Можем пересчитать пример со 128 элементами:
               n * log (n) = 128 * 7 = 896.
               Получается значительная разница (и чем больше элементов — тем она будет существеннее).
        О(n^2) — квадратичная зависимость, она ещё более медленная, чем предыдущая.
                 Если там мы умножали 128 * 7, здесь нам пришлось бы умножать 128 на 128 (128^2 = 128 * 128 = 16 384).
        О(n!) — самая медленная оценка из базовых — факториал от числа элементов, который надо обработать.
                Для обработки 128 элементов пришлось бы считать следующую цепочку:
                1 * 2 * 3 * … * 127 * 128 ~ 3,85 * 10 ** 215 — это число уже на много порядков больше
                даже предыдущего большого числа."""