import matplotlib.pyplot as plt
import seaborn as sns

# The names of the 27 devices and the percentage of unencrypted messages are stored in the following two lists respectively
devices = ['Apple_tv', 'arlo_camera_pro4', 'blink_doorbell', 'boifun_baby',
           'bose_speaker','echodot4','eufy_robovac','furbo_dog_camera',
           'google_nest_doorbell','google_nest_hub','govee_strip_light','lifx_mini',
           'nest_cam','netatmo_weather_station','nokia_tv',
           'petsafe_feeder','ring_doorbell','ring_indoor_cam','roku_tv_stick',
           'simplicam','sonos_speaker','switchbot_hub_mini','toshiba_tv',
           'weekett_kettle','withings_scale','wiz_smart_bulb','wyze_cam_pan_v2'] 
percentages = ["1.49%", "0.04%", "0.00%", "0.07%", "1.95%", "0.01%", "0.01%", "1.22%", "0.07%", "0.69%", "0.29%", "0.05%", "0.14%", "0.03%",
               "0.03%", "0.16%", "0.01%", "0.07%", "32.57%", "0.09%", "0.11%", "0.51%", "0.15%", "0.01%", "0.00%", "0.10%", "4.34%"]

# Convert percentages to decimal values
percent_values = [float(percentage.strip('%'))/100 for percentage in percentages]

plt.figure(figsize=(15, 8))

# Create a histogram
plt.bar(devices, percent_values, color='skyblue')
plt.ylabel('Unencrypted Messages Percentage')
plt.xlabel('Devices')
plt.title('Percentage of Unencrypted Messages by Device')
plt.xticks(rotation=90) 
plt.tight_layout()  
plt.show()


# Create a violin plot
sns.violinplot(x=devices, y=percent_values, palette="pastel")

plt.ylabel('Unencrypted Messages Percentage')
plt.xlabel('Devices')
plt.title('Distribution of Unencrypted Messages by Device')
plt.xticks(rotation=90) 
plt.tight_layout()
plt.show()

plt.figure(figsize=(15, 8))
