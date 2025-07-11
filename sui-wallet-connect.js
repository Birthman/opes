async function connectSuiWallet() {
  if (!window.sui) {
    alert('Sui Wallet extension not found! Please install it first.');
    return;
  }

  try {
    // Request user to connect wallet
    const accounts = await window.sui.connect();
    
    if (accounts.length === 0) {
      alert('No account found after connecting.');
      return;
    }
    
    const address = accounts[0];
    alert(`Connected wallet address: ${address}`);
    
    // Update UI button text
    const btn = document.getElementById('connectWalletBtn');
    if (btn) {
      btn.textContent = `Wallet Connected: ${address.slice(0,6)}...${address.slice(-4)}`;
      btn.disabled = true;
    }

  } catch (error) {
    console.error('Failed to connect wallet:', error);
    alert('Failed to connect wallet.');
  }
}

// Attach to button after DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const connectBtn = document.getElementById('connectWalletBtn');
  if (connectBtn) {
    connectBtn.addEventListener('click', connectSuiWallet);
  }
});
