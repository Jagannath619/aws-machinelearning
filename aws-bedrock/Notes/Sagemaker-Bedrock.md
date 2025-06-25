
---


Start
|
v
Go to SageMaker Console
|
v
Create Unified Studio Domain
|
v
[Choose Setup Option]
├──> Quick Setup
└──> Manual Setup (custom VPC, subnets)
|
v
[Configure SSO (Optional)]
├──> Use IAM credentials
└──> Use SSO (Identity Center or SAML)
|
v
Access Bedrock IDE (formerly Bedrock Studio)
|
v
Open Unified Studio (SageMaker)
|
v
Create a Project
|
v
Select "Generative AI Application Development"
|
v
Create Chat Agent App
|
v
Select Model from Dropdown
(only shows models with approved access)
|
v
Experiment with:
├──> Quick-start prompts
├──> Guardrails (content filters)
└──> Inference Parameters (Temperature, Top P)
|
v
Save App
|
v
Monitor Usage
|
v
Enable Invocation Logging
|
v
Send Logs To:
├──> CloudWatch Log Group (create if needed)
└──> S3 Bucket (optional)
|
v
Done ✅
## ✅ Key Steps

### 1. Access Bedrock IDE
- Go to AWS Console → SageMaker → Unified Studio.
- Create a **Unified Studio Domain**.

### 2. Configure Authentication
- Use **IAM credentials** or configure **SSO (optional)**.

### 3. Open Bedrock IDE
- Inside Unified Studio, launch the **Bedrock IDE**.

### 4. Create a Project
- Choose **Generative AI application development**.
- Click **Create Project** and follow the wizard.

### 5. Build a Chat Agent App
- Click **Build Chat Agent**.
- Choose from available models (only those with access).
- Adjust settings like **guardrails** and **inference parameters**.

### 6. Monitor Usage
- Use **CloudWatch Logs** or **S3** for invocation logging.
- Create a log group and IAM role as needed.

---

## 📝 Notes

- You must **request access** to each model (e.g., Claude, Titan, Jurassic-2) before it appears in the IDE dropdown.
- Bedrock IDE is now fully integrated into **SageMaker Unified Studio**.
- Monitor and optimize model usage via **CloudWatch** or export logs to **S3**.

---

## 📎 References

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)

---

