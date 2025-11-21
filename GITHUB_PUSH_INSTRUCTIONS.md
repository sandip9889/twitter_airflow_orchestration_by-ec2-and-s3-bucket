# GitHub Push Instructions

## ✅ Files to Commit to GitHub

These files are **SAFE** to commit:

```
✅ twitter_etl.py          (credentials removed - placeholders only)
✅ twitter_dag.py          (DAG definition)
✅ README.md               (comprehensive documentation)
✅ SETUP_GUIDE.md          (quick start guide)
✅ .gitignore              (prevents committing sensitive files)
✅ GITHUB_PUSH_INSTRUCTIONS.md (this file)
```

---

## ❌ Files to NEVER Commit

These files contain **SENSITIVE DATA** and should **NEVER** be committed:

```
❌ airflow_twitter_ec2.pem     (SSH private key)
❌ *.pem files                  (any SSH keys)
❌ twitter_etl.py with real credentials
❌ Any config files with API keys
```

The `.gitignore` file will automatically prevent these from being committed.

---

## 📋 Step-by-Step GitHub Push

### Step 1: Initialize Git Repository

```bash
cd d:\AIRFLOW_ETL
git init
```

### Step 2: Add Remote Repository

Create a new repository on GitHub, then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/twitter-etl-airflow.git
```

### Step 3: Stage Files

```bash
git add twitter_etl.py
git add twitter_dag.py
git add README.md
git add SETUP_GUIDE.md
git add .gitignore
git add GITHUB_PUSH_INSTRUCTIONS.md
```

### Step 4: Verify What Will Be Committed

```bash
git status
```

**Make sure you see:**
- ✅ Green files (staged for commit)
- ❌ NO .pem files
- ❌ NO files with real credentials

### Step 5: Commit Changes

```bash
git commit -m "Initial commit: Twitter ETL pipeline with Apache Airflow on AWS EC2"
```

### Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

---

## 🔒 Security Checklist

Before pushing, verify:

- [ ] No `.pem` files in the repository
- [ ] No real API keys in `twitter_etl.py`
- [ ] No real S3 bucket names (or use placeholder)
- [ ] `.gitignore` file is present
- [ ] All credentials are replaced with placeholders

---

## 📝 Recommended Commit Message

```
Initial commit: Twitter ETL pipeline with Apache Airflow on AWS EC2

Features:
- Twitter API v2 integration for tweet extraction
- Apache Airflow DAG for orchestration
- AWS S3 storage for processed data
- Comprehensive setup documentation
- Security best practices with .gitignore

Tech Stack:
- Python 3.12
- Apache Airflow 3.1.3
- Tweepy 4.16.0
- AWS EC2 (Ubuntu 24.04)
- AWS S3
```

---

## 🎯 After Pushing to GitHub

### Update Your Repository

1. Add a description on GitHub
2. Add topics/tags: `airflow`, `etl`, `twitter-api`, `aws`, `data-engineering`, `python`
3. Add a license (MIT recommended)
4. Enable GitHub Actions (optional - for CI/CD)

### Update README.md

Replace placeholders in the README:
- `[@yourusername]` → Your actual GitHub username
- `**Your Name**` → Your actual name

---

## 🚀 Optional: Create GitHub Releases

Tag your first release:

```bash
git tag -a v1.0.0 -m "First stable release"
git push origin v1.0.0
```

---

## 📊 Repository Settings

### Recommended Settings:

1. **Visibility:** Public (for portfolio) or Private (for security)
2. **Branch Protection:** Enable for `main` branch
3. **Security Alerts:** Enable Dependabot
4. **Discussions:** Enable for community support

---

## ⚠️ Important Reminders

1. **NEVER** commit the `.pem` file
2. **NEVER** commit real API credentials
3. **ALWAYS** use placeholders in public repositories
4. **REVIEW** files before committing
5. **USE** environment variables for production

---

## 🔄 Updating the Repository

When making changes:

```bash
git add .
git commit -m "Description of changes"
git push origin main
```

---

## 📞 Need Help?

If you accidentally committed sensitive data:

1. **Remove from history:**
   ```bash
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch airflow_twitter_ec2.pem" \
   --prune-empty --tag-name-filter cat -- --all
   ```

2. **Force push:**
   ```bash
   git push origin --force --all
   ```

3. **Rotate credentials immediately** (generate new API keys)

---

**Good luck with your GitHub repository! 🎉**

