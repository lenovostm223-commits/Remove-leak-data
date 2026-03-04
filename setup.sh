#!/bin/bash

echo "🚀 Setting up Dark Web Monitor on Replit"

# Install Tor via nix
echo "📦 Installing Tor..."
cat > replit.nix << EOF
{ pkgs }: {
  deps = [
    pkgs.python310
    pkgs.tor
    pkgs.torsocks
  ];
}
EOF

# Configure Tor
echo "🔧 Configuring Tor..."
cat > .torrc << EOF
SocksPort 9050
ControlPort 9051
DataDirectory /tmp/tor_data
HiddenServiceDir /home/runner/${REPL_SLUG}/tor/hidden_service
HiddenServicePort 80 127.0.0.1:5000
Log notice file /tmp/tor_notices.log
EOF

# Create run script
echo "📝 Creating run script..."
cat > run.sh << EOF
#!/bin/bash
tor -f .torrc &
sleep 5
python main.py
EOF

chmod +x run.sh

# Install Python dependencies
echo "🐍 Installing Python packages..."
pip install -r requirements.txt

echo "✅ Setup complete! Click Run to start"
echo "🌐 Your .onion domain will appear in the console"
