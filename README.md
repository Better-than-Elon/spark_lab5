### Main file: cluster.py
```
$ poetry run python cluster.py
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
24/06/29 13:35:31 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
2024-06-29 13:35:43,973 — data_processing — INFO — Input data
root
 |-- completeness: double (nullable = false)
 |-- energy_100g: double (nullable = false)
 |-- energy-kcal_100g: double (nullable = false)
 |-- carbohydrates_100g: double (nullable = false)
 |-- proteins_100g: double (nullable = false)
 |-- fat_100g: double (nullable = false)
 |-- sugars_100g: double (nullable = false)
 |-- saturated-fat_100g: double (nullable = false)
 |-- salt_100g: double (nullable = false)
 |-- sodium_100g: double (nullable = false)

2024-06-29 13:35:45,110 — data_processing — INFO — VectorAssembler
+----------------------------------------+
|                                features|
+----------------------------------------+
|                          (10,[0],[0.3])|
|[0.2625,690.0,165.0,65.0,1.5,2.0,12.6...|
|[0.4875,0.0,0.0,9.8,2.7,1.4,9.8,0.9,0...|
|[0.575,238.0,57.0,3.9,10.0,0.2,3.9,0....|
|[0.275,1569.0,375.0,70.1,7.8,7.0,15.0...|
+----------------------------------------+
only showing top 5 rows

2024-06-29 13:35:46,977 — data_processing — INFO — StandardScaler
+----------------------------------------+
|                          scaledFeatures|
+----------------------------------------+
|           (10,[0],[1.7706162899459679])|
|[1.549289253702722,0.1673175525011161...|
|[2.877251471162198,0.0,0.0,0.23256892...|
|[3.393681222396438,0.0577124311525589...|
|[1.6230649324504707,0.380465565035146...|
+----------------------------------------+
only showing top 5 rows

24/06/29 13:35:49 WARN InstanceBuilder: Failed to load implementation from:dev.ludovic.netlib.blas.JNIBLAS
2024-06-29 13:35:53,542 — data_processing — INFO — Silhouette Score for k = 12 is 0.3569635460363891
SUCCESS: The process with PID 19480 (child process of PID 11348) has been terminated.
SUCCESS: The process with PID 11348 (child process of PID 20668) has been terminated.
SUCCESS: The process with PID 20668 (child process of PID 20828) has been terminated.
```