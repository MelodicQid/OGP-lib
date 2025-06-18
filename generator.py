def generate_key_path(observers):
    """
    Given a list of Observer instances, returns a structure that represents
    the recursive path and the final emergent key.
    """
    path = []
    for obs in observers:
        path.append({
            "level": obs.level,
            "state": obs.state
        })
    key = hash(tuple(obs.state for obs in observers)) % 9973
    return {
        "path": path,
        "key": key
    }
