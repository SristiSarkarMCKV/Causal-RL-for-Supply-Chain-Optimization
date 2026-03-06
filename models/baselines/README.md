1. 𝗘𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁 𝗮𝗻𝗱 𝗣𝗼𝗹𝗶𝗰𝘆 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻

𝗪𝗵𝗮𝘁 𝗜 𝗱𝗶𝗱:
I implemented a `SlInventoryPolicy` class representing a 3-node supply chain (Supplier → Warehouse → Retailer) and coded a classic (𝘀, 𝗦) 𝗶𝗻𝘃𝗲𝗻𝘁𝗼𝗿𝘆 𝗽𝗼𝗹𝗶𝗰𝘆. I set the reorder point 𝘀 at 500 units and the order-up-to level 𝗦 at 1000 units.

𝗪𝗵𝘆 𝗜 𝗱𝗶𝗱 𝗶𝘁:
We need a "common sense" baseline to compare against future Reinforcement Learning agents. The (𝘀,𝗦) policy is a standard industry heuristic where an order is triggered only when inventory falls below 𝘀, bringing it back up to 𝗦.

𝗦𝗼 𝘄𝗵𝗮𝘁:
This gives us a controlled environment to measure the impact of lead times and holding costs. By fixing these parameters, we can clearly see how traditional logic handles the demand volatility identified in the EDA.



2. 𝟱𝟮-𝗪𝗲𝗲𝗸 𝗦𝗶𝗺𝘂𝗹𝗮𝘁𝗶𝗼𝗻 𝗟𝗼𝗴𝗶𝗰

𝗪𝗵𝗮𝘁 𝗜 𝗱𝗶𝗱:
I built a simulation loop that runs for 𝟱𝟮 𝘄𝗲𝗲𝗸𝘀, processing weekly aggregated demand from the DataCo dataset. The simulation tracks "pipeline orders" (orders placed but not yet arrived) and applies a 𝟮-𝘄𝗲𝗲𝗸 𝗹𝗲𝗮𝗱 𝘁𝗶𝗺𝗲 for arrivals.

𝗪𝗵𝘆 𝗜 𝗱𝗶𝗱 𝗶𝘁:
A year-long simulation captures the seasonality and "demand spikes" we found earlier. The pipeline tracking is crucial because, in the real world, you can't ignore the inventory that is currently in transit.

𝗦𝗼 𝘄𝗵𝗮𝘁:
This setup allows us to calculate the 𝗙𝗶𝗹𝗹 𝗥𝗮𝘁𝗲 𝗮𝗻𝗱 𝗧𝗼𝘁𝗮𝗹 𝗖𝗼𝘀𝘁 (Holding + Stockout + Ordering). It moves the project from static data analysis to a dynamic "What-If" scenario.



3. 𝗕𝗮𝘀𝗲𝗹𝗶𝗻𝗲 𝗣𝗲𝗿𝗳𝗼𝗿𝗺𝗮𝗻𝗰𝗲 𝗥𝗲𝘀𝘂𝗹𝘁𝘀

𝗪𝗵𝗮𝘁 𝗜 𝗱𝗶𝗱:
I ran the simulation using the DataCo `Order Item Quantity` as the demand signal. The baseline achieved a 𝗧𝗼𝘁𝗮𝗹 𝗖𝗼𝘀𝘁 𝗼𝗳 𝟭,𝟮𝟯𝟳,𝟱𝟮𝟵.𝟮𝟵 and a 𝗙𝗶𝗹𝗹 𝗥𝗮𝘁𝗲 𝗼𝗳 𝟵𝟰.𝟮𝟭%.

𝗪𝗵𝘆 𝗜 𝗱𝗶𝗱 𝗶𝘁:
To establish the "score to beat." A 94% fill rate is decent, but the high total cost suggests that the fixed 𝘀 and 𝗦 parameters may be causing either excessive holding costs or expensive emergency orders during spikes.

𝗦𝗼 𝘄𝗵𝗮𝘁:
We now have a benchmark. Any RL agent we train must either way 𝗿𝗲𝗱𝘂𝗰𝗲 𝘁𝗵𝗮𝘁 𝗺𝗶𝗹𝗹𝗶𝗼𝗻-𝗱𝗼𝗹𝗹𝗮𝗿 𝗰𝗼𝘀𝘁 or 𝗶𝗺𝗽𝗿𝗼𝘃𝗲 𝘁𝗵𝗲 𝘀𝗲𝗿𝘃𝗶𝗰𝗲 𝗹𝗲𝘃𝗲𝗹 𝗯𝗲𝘆𝗼𝗻𝗱 𝟵𝟰% to be considered successful. The fact that 6% of demand is still unfulfilled suggests there is room for a "smarter" policy that anticipates the spikes we saw in the EDA.
