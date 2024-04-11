from scipy.stats import pearsonr, spearmanr

original = [36, -16, -24, 4]
reproduction = [23, -8.67, -17.89, 3.56]

# Calculating Pearson's r
pearson_corr, p_value_pearson = pearsonr(original, reproduction)

# Calculating Spearman's rho
spearman_corr, p_value_spearman = spearmanr(original, reproduction)

print(f"Pearson's r: {pearson_corr}, p-value: {p_value_pearson}")
print(f"Spearman's rho: {spearman_corr}, p-value: {p_value_spearman}")
