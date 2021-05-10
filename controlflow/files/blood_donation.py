age = 34
weight = 81
hearbeat = 70
platelets = 200_000

age_req = 18 <= age <= 65
weight_req = weight > 55
hearbeat_req = 50 <= hearbeat <= 110
platelets_req = platelets >= 150_000

if age_req and weight_req and hearbeat_req and platelets_req:
    print('Apto para donar sangre')
else:
    print('No apto para donar sangre')
