% Perform t-test for the difference in stimulation effects between depression and Parkinson's
[~, p_value_diff, ~, stats_diff] = ttest2(meg_post(:) - meg_baseline_alpha(:), meg_post_beta(:) - meg_baseline_beta(:));

% Display the p-value and other relevant information
disp(['P-value for t-test for the difference between Depression and Parkinson''s: ', num2str(p_value_diff)]);
disp(['t-statistic for the difference: ', num2str(stats_diff.tstat)]);
disp(['Degrees of freedom for the difference: ', num2str(stats_diff.df)]);

% Display whether the null hypothesis is rejected for the difference
if p_value_diff < 0.05
    disp('Reject the null hypothesis: There is a significant difference in the effects of stimulation between Depression and Parkinson''s.');
else
    disp('Fail to reject the null hypothesis: There is no significant difference in the effects of stimulation between Depression and Parkinson''s.');
end

