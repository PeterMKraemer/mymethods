import numpy as np

# Wiener Diffusion Model rng (c) by Laura Fontanesi.
def DM_rng_mat(drift, threshold, ndt, rel_sp=.5, noise_constant=1, dt=0.001, max_rt=5):
    shape = drift.shape

    acc = np.empty(shape) * np.nan
    rt = np.empty(shape) * np.nan
    rel_sp = np.ones(shape) * rel_sp
    max_tsteps = max_rt / dt

    # condition for existence:
    bad = np.logical_or(rel_sp < 0, rel_sp > 1)
    bad = np.logical_or(bad, threshold <= 0)
    bad = np.logical_or(bad, ndt < 0)

    # initialisation
    x = np.ones(shape) * rel_sp * threshold
    tstep = 0
    ongoing = np.array(np.ones(shape), dtype=bool)
    ongoing[bad] = False

    # start accumulation process
    while np.sum(ongoing) > 0 and tstep < max_tsteps:
        x[ongoing] += np.random.normal(drift[ongoing] * dt, noise_constant * (dt ** (1 / 2)), np.sum(ongoing))
        tstep += 1

        # ended trials
        ended_correct = (x >= threshold)
        ended_incorrect = (x <= 0)

        # store results and filter out ended trials
        if np.sum(ended_correct) > 0:
            acc[np.logical_and(ended_correct, ongoing)] = 1
            rt[np.logical_and(ended_correct, ongoing)] = dt * tstep + ndt[np.logical_and(ended_correct, ongoing)]
            ongoing[ended_correct] = False

        if np.sum(ended_incorrect) > 0:
            acc[np.logical_and(ended_incorrect, ongoing)] = 0
            rt[np.logical_and(ended_incorrect, ongoing)] = dt * tstep + ndt[np.logical_and(ended_incorrect, ongoing)]
            ongoing[ended_incorrect] = False

    return rt, acc