# Pre-Push Checklist ✅

## Before Pushing to GitHub, Verify:

### 🔒 Security Check (CRITICAL!)

- [ ] **NO .pem files** in the repository
- [ ] **NO real API keys** in any files
- [ ] **NO real AWS credentials** in any files
- [ ] **NO real S3 bucket names** (or use placeholder)
- [ ] `.gitignore` file is present and configured
- [ ] All credentials replaced with `YOUR_*_HERE` placeholders

### 📁 Files to Include

- [ ] `twitter_etl.py` (with placeholders, no real credentials)
- [ ] `twitter_dag.py` (DAG definition)
- [ ] `README.md` (comprehensive documentation)
- [ ] `SETUP_GUIDE.md` (quick start guide)
- [ ] `.gitignore` (security file)
- [ ] `GITHUB_PUSH_INSTRUCTIONS.md` (push guide)
- [ ] `PROJECT_SUMMARY.md` (project overview)
- [ ] `PRE_PUSH_CHECKLIST.md` (this file)

### ❌ Files to EXCLUDE

- [ ] `airflow_twitter_ec2.pem` (SSH key - NEVER commit!)
- [ ] Any `*.pem` files
- [ ] `import tweepy.new.py` (old test file)
- [ ] Any files with real credentials
- [ ] `__pycache__/` directories
- [ ] `.env` files

### 📝 Documentation Check

- [ ] README.md has clear setup instructions
- [ ] All code has comments explaining functionality
- [ ] Troubleshooting section is complete
- [ ] Prerequisites are clearly listed
- [ ] Architecture diagram is included

### 🎨 Personalization

- [ ] Replace `[@yourusername]` with your GitHub username
- [ ] Replace `**Your Name**` with your actual name
- [ ] Add your email/contact info (optional)
- [ ] Customize project description if needed

### 🧪 Final Verification

Run these commands to verify:

```bash
# Check what will be committed
git status

# View the .gitignore file
cat .gitignore

# Search for potential credentials (should return nothing)
grep -r "AAAA" *.py
grep -r "sk-" *.py

# Verify .pem files are ignored
git check-ignore airflow_twitter_ec2.pem
```

Expected output for last command: `airflow_twitter_ec2.pem` (means it's ignored ✅)

### 🚀 Ready to Push?

If all boxes are checked ✅, you're ready to push!

```bash
git init
git add .
git status  # Review one more time!
git commit -m "Initial commit: Twitter ETL pipeline with Apache Airflow on AWS EC2"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/twitter-etl-airflow.git
git push -u origin main
```

---

## ⚠️ If You Find Issues

### Found credentials in files?
1. Remove them immediately
2. Replace with placeholders
3. DO NOT commit yet

### Found .pem file staged?
1. Run: `git reset HEAD airflow_twitter_ec2.pem`
2. Verify `.gitignore` includes `*.pem`
3. Run: `git status` to confirm it's not staged

### Accidentally committed sensitive data?
1. **DO NOT PUSH** to GitHub yet
2. Run: `git reset --soft HEAD~1` (undo last commit)
3. Remove sensitive data
4. Commit again

---

## 🎯 Post-Push Tasks

After successfully pushing:

- [ ] Verify repository on GitHub (check files are there)
- [ ] Add repository description on GitHub
- [ ] Add topics/tags: `airflow`, `etl`, `twitter-api`, `aws`, `python`
- [ ] Add a license (MIT recommended)
- [ ] Star your own repository (why not? 😄)
- [ ] Share on LinkedIn/Twitter (optional)

---

## 📊 Repository Settings (on GitHub)

### Recommended:
- **Visibility:** Public (for portfolio)
- **Include README:** Yes
- **License:** MIT License
- **Topics:** airflow, etl, data-engineering, aws, python, twitter-api

### Optional:
- Enable GitHub Discussions
- Enable Issues
- Add project description
- Add website link (if you have a portfolio)

---

## 🎉 Success Criteria

Your repository is ready when:

✅ All files are committed and pushed
✅ No sensitive data is exposed
✅ README is clear and comprehensive
✅ Code is well-documented
✅ .gitignore is working correctly
✅ Repository looks professional

---

## 🆘 Emergency: Exposed Credentials

If you accidentally pushed credentials:

### Immediate Actions:
1. **Rotate ALL credentials immediately**
   - Generate new Twitter API keys
   - Generate new AWS access keys
   - Generate new EC2 key pair

2. **Remove from Git history**
   ```bash
   git filter-branch --force --index-filter \
   "git rm --cached --ignore-unmatch FILENAME" \
   --prune-empty --tag-name-filter cat -- --all
   
   git push origin --force --all
   ```

3. **Contact GitHub Support** if needed

---

## ✅ Final Check

Before clicking "Push":

**Ask yourself:**
- Would I be comfortable if my boss/recruiter saw this?
- Are there any secrets or credentials visible?
- Is the documentation clear and professional?
- Does this represent my best work?

If YES to all → **PUSH!** 🚀

If NO to any → **Fix it first!** 🔧

---

**Good luck! You've got this! 💪**

