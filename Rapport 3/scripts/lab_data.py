from numpy import *
import FYS2150lib as fys


def weights():
    # Mass of weights measured with balance
    m_a_balance = 500.1e-3
    m_b_balance = 1000.3e-3
    m_c_balance = 2000.5e-3

    # Mass of reference weights
    m_reference = array([0.5, 1.0, 2.0])
    m_reference_balance = array([500.0e-3, 999.9e-3, 2000.1e-3])  # Weighed

    a, b, da, db = fys.linfit(m_reference, m_reference_balance)

    m_a = (m_a_balance - b) / a
    m_b = (m_b_balance - b) / a
    m_c = (m_c_balance - b) / a

    return m_a, m_b, m_c
