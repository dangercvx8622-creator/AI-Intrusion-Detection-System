import pandas as pd
import numpy as np

# Load dataset (replace with your path)
df = pd.read_csv('path/to/CIC-IDS2017/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')

# Basic preprocessing: Handle missing values, encode categorical features
df.dropna(inplace=True)
df['Protocol'] = df['Protocol'].astype('category').cat.codes  # Encode protocol as numbers
df['Label'] = df['Label'].apply(lambda x: 1 if 'Attack' in x else 0)  # Binary label: 0=normal, 1=attack

# Feature engineering: Add statistical features
df['Packet_Size_Mean'] = df.groupby('Flow ID')['Total Length of Fwd Packets'].transform('mean')
df['Packet_Size_Var'] = df.groupby('Flow ID')['Total Length of Fwd Packets'].transform('var')
df['Flow_Duration_Log'] = np.log1p(df['Flow Duration'])  # Log transform for normalization

# Select top features (expand to 50+ based on domain knowledge)
features = [
    'Flow Duration', 'Total Fwd Packets', 'Total Backward Packets', 'Total Length of Fwd Packets',
    'Total Length of Bwd Packets', 'Fwd Packet Length Max', 'Bwd Packet Length Max',
    'Packet_Size_Mean', 'Packet_Size_Var', 'Flow_Duration_Log', 'Protocol',
    # Add more: e.g., 'SYN Flag Count', 'ACK Flag Count', etc.
]
X = df[features]
y = df['Label']

# Save processed data
X.to_csv('processed_features.csv', index=False)
y.to_csv('labels.csv', index=False)
print(f"Extracted {len(features)} features from {len(df)} samples.")