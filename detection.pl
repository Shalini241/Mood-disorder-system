%% ----------------------------------
%% Major Depressive Disorder Model
%% ----------------------------------

symptom_MDD(sleep_changes).
symptom_MDD(interest_loss).
symptom_MDD(guilt).
symptom_MDD(energy_lack).
symptom_MDD(concentration_reduced).
symptom_MDD(appetite_change).
symptom_MDD(psychomotor_change).
symptom_MDD(suicidal_thoughts).

medication(copper_overload).
medication(wilson_disease).
medication(hypothyroidism).

substance_usage(alcohol).
substance_usage(drugs).
substance_usage(opioid).


duration_for_MDD_in_days :- duration(N), N>=14.


medical_condition :- medication(X), medical_condition_user(X).
substance_condition :- substance_usage(X), substance_usage_user(alcohol).


have_all_MDD_symptomps :- #count{ Symptom : symptom_MDD(Symptom), possible_symptom(Symptom)} >= 5.
diagnosis_with_MDD :- have_all_MDD_symptomps, duration_for_MDD_in_days, not ab_diagnosis_with_MDD, not -diagnosis_with_MDD.

-diagnosis_with_MDD :- not possible_symptom(interest_loss).

ab_diagnosis_with_MDD :- medical_condition.
ab_diagnosis_with_MDD :- substance_condition.




%% ------------------
%% Mania Model
%% ------------------

symptom_Mania(distractible).
symptom_Mania(irresponsibility).
symptom_Mania(grandiose).
symptom_Mania(energy_lack).
symptom_Mania(flight_of_ideas).
symptom_Mania(activity_increase).
symptom_Mania(sleep_decrease).
symptom_Mania(talkative).
symptom_Mania(social_impairment).

duration_for_Mania_in_days :- duration(N), N>=7.

have_all_Mania_symptomps :- #count{ Symptom : symptom_Mania(Symptom), possible_symptom(Symptom)} >= 4.
diagnosis_with_Mania :- have_all_Mania_symptomps, duration_for_Mania_in_days, not ab_diagnosis_with_Mania, not -diagnosis_with_Mania.

-diagnosis_with_Mania :- not possible_symptom(social_impairment).

ab_diagnosis_with_Mania :- medical_condition.
ab_diagnosis_with_Mania :- substance_condition.

#show diagnosis_with_MDD/0.
#show -diagnosis_with_MDD/0.
#show diagnosis_with_Mania/0.
#show -diagnosis_with_Mania/0.


%-------- Inputs -----------%

possible_symptom(psychomotor_change).
possible_symptom(suicidal_thoughts).
possible_symptom(energy_lack).
possible_symptom(sleep_changes).
possible_symptom(appetite_change).
possible_symptom(interest_loss).
possible_symptom(flight_of_ideas).
possible_symptom(activity_increase).
possible_symptom(sleep_decrease).
possible_symptom(talkative).
possible_symptom(social_impairment).

duration(15).

%-------- Inputs -----------%



