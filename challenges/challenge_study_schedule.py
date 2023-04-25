def study_schedule(permanence_period, target_time):
    try:
        result = [
            start
            for start, end in permanence_period
            if start <= target_time <= end
        ]
        return len(result)
    except TypeError:
        return None
