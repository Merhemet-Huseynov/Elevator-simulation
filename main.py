from process_simulation import simulation
import datetime

# Start and end times
start = datetime.datetime.now()
end = start + datetime.timedelta(minutes=1)

# Period
while start <= end:
    sim_result = simulation()
    print(sim_result)
