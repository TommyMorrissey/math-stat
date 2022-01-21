# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 14:51:07 2022

@author: tmorrissey
"""

"""
Table of Contents:
    1) Introduction
    2) Model Fitting
    3) Exponential Family and Generalized Linear Models
    4) Estimation
    5) Inference
    6) Normal Linear Models
    7) Binary Variables and Logistic Regression
    8) Nominal and Ordinal Logistic Regression
    9) Poisson Regression and Log-Linear Models
    10) Survival Analysis
    11) Clustered and Longitudinal Data
    12) Bayesian Analysis
    13) Markov Chain Monte Carlo Methods
    14) Example Bayesian Analyses
    

Introduction to Generalized Linear Models

Definitions:

    Dependent Variable - a.k.a response, outcome - variable that changes due to other variables, what is being tested
    Independent Variable - a.k.a. explanatory, predictor - does not change due to impact of other variables

Data Types:
    
    Nominal - examples: yes, no, red, yellow, green
        Includes: Binary, Binomial, Multinomial variables
    Ordinal - ranking between categories e.g. young, middle aged, old, 0 - 70, 71 - 100, etc.
    Continuous - values (in theory) fall anywhere on a contiuum e.g. weight, time, length etc.
    Nominal & Ordinal are sometimes called Categorical or Discrete variables
"""