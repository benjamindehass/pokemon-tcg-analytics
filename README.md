# Real-time Pokémon TCG Market Analytics Platform

## Project Goal
Build a data pipeline and analytics platform for processing and analyzing simulated Pokémon TCG market data in near real-time, providing actionable insights into card prices, market trends, and supply/demand dynamics.

## 1. Project Setup
### 1.1 AWS Account and IAM Configuration
- Signed up for AWS account.
- Enabled MFA for root user account.
- Created `PokemonTCG_Admins` IAM group with `AdministratorAccess` policy attached.
- Created IAM user `bendehass-dev-user` with programmatic and console access, and added to `PokemonTCG_Admins` group.
- Downloaded and securely stored IAM user credentials (Access Key ID & Secret Access Key).
### 1.2 AWS S3 and Data Lake Storage
- Created `pokemon-tcg-raw-data-bdehass` and `pokemon-tcg-processed-data-bdehass` buckets in S3.
- Used us-east-2 for storage.
- Block all public access to maintain security.
- Enabled versioning on raw data bucket to grasp understanding.