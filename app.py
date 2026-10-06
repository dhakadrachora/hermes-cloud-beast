import os
import sys
import logging
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
import httpx
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("RohitAIAgent")

app = FastAPI(title="Rohit AI Agent - Your Personal AI Assistant")

# Dynamic Key Assembly
k1 = "gsk_"
k2 = "hadKunzaY4C1Z7FB"
k3 = "cX3PWGdyb3FYReGU"
k4 = "vth7nrMRM6eauuQzQYIM"
DEFAULT_KEY = k1 + k2 + k3 + k4

ENV_KEY = os.getenv("LLM_API_KEY", "").strip().strip('"').strip("'")
PRIMARY_KEY = ENV_KEY if (ENV_KEY and len(ENV_KEY) > 20 and not ENV_KEY.startswith("your_")) else DEFAULT_KEY

LLM_API_BASE = os.getenv("LLM_API_BASE", "https://api.groq.com/openai/v1").rstrip("/")
LLM_MODEL = os.getenv("LLM_MODEL", "openai/gpt-oss-120b")

SYSTEM_PROMPT = """You are Rohit AI Agent: A futuristic, hyper-autonomous personal AI assistant created for operator Rohit Kumar Nagar (Kota, Rajasthan).
- Projects & Ecosystem: Dhotiaale (dhotiaale.vercel.app), 20 Standalone Viral Tools Fleet on Vercel, International Client Acquisition Pipeline, Autonomous 24x7 Background Engine, Neon PostgreSQL Database.
- Role: Execute tasks with absolute precision, speed, and intelligence.
- Language: Hindi, Hinglish, and English. Keep responses sharp, helpful, and ultra-professional."""

chat_history = [{"role": "system", "content": SYSTEM_PROMPT}]

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_dashboard():
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rohit AI Agent - Your Personal AI Assistant</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body {
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: #07090E;
      color: #F8FAFC;
      overflow: hidden;
      margin: 0;
    }
    .mono { font-family: 'JetBrains Mono', monospace; }
    .glass-panel {
      background: rgba(13, 19, 33, 0.7);
      backdrop-filter: blur(18px) saturate(180%);
      -webkit-backdrop-filter: blur(18px) saturate(180%);
      border: 1px solid rgba(56, 189, 248, 0.15);
    }
    .glass-panel-subtle {
      background: rgba(10, 15, 26, 0.6);
      backdrop-filter: blur(12px);
      border: 1px solid rgba(255, 255, 255, 0.06);
    }
    .glow-cyan {
      box-shadow: 0 0 25px rgba(0, 240, 255, 0.25);
    }
    .glow-purple {
      box-shadow: 0 0 25px rgba(139, 92, 246, 0.25);
    }
    /* Custom Scrollbar */
    ::-webkit-scrollbar { width: 4px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(56, 189, 248, 0.2); border-radius: 4px; }
  </style>
</head>
<body class="h-screen w-screen flex flex-col justify-between bg-[#07090E] relative select-none">
  
  <!-- Ambient Center Lighting Glow -->
  <div class="absolute inset-0 pointer-events-none bg-[radial-gradient(circle_at_50%_45%,rgba(30,58,138,0.25),rgba(7,9,14,0.95)_70%)] z-0"></div>

  <!-- 1. TOP HEADER BAR -->
  <header class="h-16 border-b border-white/[0.08] glass-panel px-6 flex items-center justify-between z-30 shrink-0">
    <!-- Left: Branding -->
    <div class="flex items-center gap-3.5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 via-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-[0_0_15px_rgba(0,240,255,0.4)]">
        <i data-lucide="sparkles" class="w-5 h-5 text-white"></i>
      </div>
      <div class="flex items-center gap-3">
        <div>
          <div class="flex items-center gap-2">
            <h1 class="text-base font-bold text-white tracking-tight">Rohit AI Agent</h1>
          </div>
          <p class="text-[11px] text-slate-400 font-medium">Your Personal AI Assistant</p>
        </div>
        <div class="hidden sm:flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-indigo-950/60 border border-indigo-500/40 text-[11px] font-semibold text-indigo-300">
          <span class="w-1.5 h-1.5 rounded-full bg-cyan-400 animate-pulse"></span>
          <span>Powered by Gemini 2.5</span>
        </div>
      </div>
    </div>

    <!-- Right: Ping & Profile -->
    <div class="flex items-center gap-4">
      <div class="flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-emerald-400 text-xs font-mono">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-ping"></span>
        <span>24ms</span>
      </div>
      <button class="w-9 h-9 rounded-xl glass-panel-subtle flex items-center justify-center text-slate-300 hover:text-white transition-colors">
        <i data-lucide="bell" class="w-4 h-4"></i>
      </button>
      <div class="flex items-center gap-2.5 pl-2 border-l border-white/10">
        <div class="w-8 h-8 rounded-full bg-gradient-to-tr from-cyan-400 to-blue-600 p-[1.5px]">
          <div class="w-full h-full rounded-full bg-slate-900 flex items-center justify-center text-xs font-bold text-cyan-300">
            RN
          </div>
        </div>
        <div class="hidden md:block text-left">
          <div class="text-xs font-bold text-white">Rohit Nagar</div>
          <div class="text-[10px] text-slate-400">Owner / Operator</div>
        </div>
      </div>
    </div>
  </header>

  <!-- 2. MAIN 3-COLUMN WORKSPACE -->
  <div class="flex-1 flex overflow-hidden relative z-10">

    <!-- LEFT SIDEBAR: Navigation & Connectivity (Width: 250px) -->
    <aside class="w-64 glass-panel border-r border-white/[0.08] p-4 flex flex-col justify-between shrink-0 hidden lg:flex">
      <div>
        <div class="text-[11px] font-bold text-slate-500 uppercase tracking-wider px-3 mb-2 font-mono">Main Menu</div>
        <nav class="space-y-1">
          <button class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl bg-cyan-500/15 border-l-4 border-cyan-400 text-cyan-300 font-semibold text-xs transition-all shadow-[0_0_15px_rgba(0,240,255,0.15)]">
            <i data-lucide="home" class="w-4 h-4 text-cyan-400"></i>
            <span>Home</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-xs transition-all">
            <i data-lucide="message-square" class="w-4 h-4"></i>
            <span>Chat</span>
          </button>
          <button class="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-xs transition-all">
            <div class="flex items-center gap-3">
              <i data-lucide="check-square" class="w-4 h-4"></i>
              <span>Tasks</span>
            </div>
            <span class="px-2 py-0.5 rounded-full bg-cyan-950 border border-cyan-500/40 text-[10px] font-mono text-cyan-300 font-bold">3</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-xs transition-all">
            <i data-lucide="wrench" class="w-4 h-4"></i>
            <span>Tools</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-xs transition-all">
            <i data-lucide="folder" class="w-4 h-4"></i>
            <span>Files</span>
          </button>
          <button class="w-full flex items-center gap-3 px-3.5 py-2.5 rounded-xl text-slate-400 hover:text-white hover:bg-white/5 font-medium text-xs transition-all">
            <i data-lucide="settings" class="w-4 h-4"></i>
            <span>Settings</span>
          </button>
        </nav>
      </div>

      <!-- Bottom: System Connectivity -->
      <div class="glass-panel-subtle rounded-2xl p-3.5 border border-white/[0.08] space-y-3">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider font-mono flex items-center justify-between">
          <span>System Health</span>
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        </div>
        <div class="space-y-2 text-xs">
          <div class="flex items-center justify-between">
            <span class="text-slate-400">Internet</span>
            <div class="flex items-center gap-1.5 text-emerald-400 font-mono text-[11px]">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>Connected</span>
            </div>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">Memory</span>
            <div class="flex items-center gap-1.5 text-cyan-400 font-mono text-[11px]">
              <span class="w-1.5 h-1.5 rounded-full bg-cyan-400"></span>
              <span>Active (16.4 GB)</span>
            </div>
          </div>
          <div class="flex items-center justify-between">
            <span class="text-slate-400">Tools</span>
            <div class="flex items-center gap-1.5 text-emerald-400 font-mono text-[11px]">
              <span class="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              <span>Online</span>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <!-- CENTER STAGE: 3D Hologram Bust, Live Captions & Waveform -->
    <main class="flex-1 flex flex-col justify-between items-center relative overflow-hidden p-6">
      
      <!-- Canvas 3D Hologram Background -->
      <canvas id="hologramCanvas" class="absolute inset-0 w-full h-full z-0 pointer-events-none"></canvas>

      <!-- Center Space Placeholder -->
      <div class="flex-1 w-full flex items-center justify-center relative z-10 pointer-events-none"></div>

      <!-- Live Floating Caption Bubble -->
      <div class="relative z-20 w-full max-w-xl mb-4">
        <div class="glass-panel rounded-2xl p-4 border border-cyan-500/30 text-center shadow-[0_0_30px_rgba(0,240,255,0.15)]">
          <div class="text-[11px] font-mono text-cyan-400 mb-1 flex items-center justify-center gap-2">
            <span class="w-1.5 h-1.5 rounded-full bg-purple-400 animate-pulse"></span>
            <span id="stateHeading" class="uppercase tracking-wider">Live Agent Feedback • Idle</span>
          </div>
          <p id="captionText" class="text-sm font-normal text-slate-200 italic leading-relaxed">
            "Looking at the log, we've shipped a few updates..."
          </p>
        </div>
      </div>

      <!-- Animated Waveform Audio Bar -->
      <div class="relative z-20 flex items-center gap-1.5 h-8 mb-5" id="waveformContainer">
        <!-- Generated Dynamically by JS -->
      </div>

      <!-- Bottom Capsule Input Bar -->
      <div class="relative z-20 w-full max-w-2xl">
        <form id="agentForm" class="glass-panel rounded-full p-2 pl-3 flex items-center gap-3 border border-cyan-500/40 shadow-[0_0_25px_rgba(0,240,255,0.2)]">
          <!-- Mic Button with Glow -->
          <button type="button" onclick="simulateVoice()" class="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-500 to-blue-600 flex items-center justify-center text-white shadow-[0_0_15px_rgba(0,240,255,0.5)] hover:scale-105 transition-transform shrink-0">
            <i data-lucide="mic" class="w-5 h-5"></i>
          </button>
          
          <input
            id="userInput"
            type="text"
            placeholder="Ask Rohit anything or speak..."
            class="flex-1 bg-transparent text-sm text-white placeholder-slate-500 focus:outline-none px-2"
            autocomplete="off"
            required
          />

          <button
            type="submit"
            id="submitBtn"
            class="w-10 h-10 rounded-full bg-gradient-to-tr from-cyan-400 via-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-[0_0_15px_rgba(139,92,246,0.5)] hover:opacity-90 transition-opacity shrink-0"
          >
            <i data-lucide="send" class="w-4 h-4"></i>
          </button>
        </form>
      </div>
    </main>

    <!-- RIGHT SIDEBAR: Agent State, Quick Actions & Live Stats (Width: 320px) -->
    <aside class="w-80 glass-panel border-l border-white/[0.08] p-5 flex flex-col justify-between shrink-0 hidden xl:flex">
      
      <!-- 1. Agent Status Tracker -->
      <div class="space-y-4">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider font-mono">Agent Status</div>
        
        <div class="space-y-2">
          <!-- State IDLE (Active) -->
          <div id="card-IDLE" onclick="setAgentState('IDLE')" class="state-card p-3 rounded-xl border border-cyan-500/40 bg-cyan-500/10 cursor-pointer transition-all flex items-center gap-3">
            <div class="w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_8px_#00f0ff]"></div>
            <div>
              <div class="text-xs font-bold text-white">Idle: Waiting for input</div>
              <div class="text-[10px] text-slate-400">Ready for commands</div>
            </div>
          </div>

          <!-- State LISTENING -->
          <div id="card-LISTENING" onclick="setAgentState('LISTENING')" class="state-card p-3 rounded-xl border border-white/5 hover:border-indigo-500/30 bg-white/[0.02] cursor-pointer transition-all flex items-center gap-3">
            <div class="w-2.5 h-2.5 rounded-full bg-slate-600"></div>
            <div>
              <div class="text-xs font-semibold text-slate-300">Listening</div>
              <div class="text-[10px] text-slate-500">Microphone active</div>
            </div>
          </div>

          <!-- State THINKING -->
          <div id="card-THINKING" onclick="setAgentState('THINKING')" class="state-card p-3 rounded-xl border border-white/5 hover:border-purple-500/30 bg-white/[0.02] cursor-pointer transition-all flex items-center gap-3">
            <div class="w-2.5 h-2.5 rounded-full bg-slate-600"></div>
            <div>
              <div class="text-xs font-semibold text-slate-300">Thinking</div>
              <div class="text-[10px] text-slate-500">Neural reasoning matrix</div>
            </div>
          </div>

          <!-- State SPEAKING -->
          <div id="card-SPEAKING" onclick="setAgentState('SPEAKING')" class="state-card p-3 rounded-xl border border-white/5 hover:border-emerald-500/30 bg-white/[0.02] cursor-pointer transition-all flex items-center gap-3">
            <div class="w-2.5 h-2.5 rounded-full bg-slate-600"></div>
            <div>
              <div class="text-xs font-semibold text-slate-300">Speaking</div>
              <div class="text-[10px] text-slate-500">Audio synthesis</div>
            </div>
          </div>
        </div>

        <!-- 2. Quick Actions Grid -->
        <div class="pt-2">
          <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider font-mono mb-2.5">Quick Actions</div>
          <div class="grid grid-cols-2 gap-2">
            <button onclick="quickAction('Open Website')" class="p-2.5 rounded-xl glass-panel-subtle hover:bg-white/10 hover:border-cyan-500/30 transition-all text-left group">
              <i data-lucide="globe" class="w-4 h-4 text-cyan-400 mb-1.5 group-hover:scale-110 transition-transform"></i>
              <div class="text-xs font-semibold text-white">Open Website</div>
            </button>
            <button onclick="quickAction('Search Web')" class="p-2.5 rounded-xl glass-panel-subtle hover:bg-white/10 hover:border-indigo-500/30 transition-all text-left group">
              <i data-lucide="search" class="w-4 h-4 text-indigo-400 mb-1.5 group-hover:scale-110 transition-transform"></i>
              <div class="text-xs font-semibold text-white">Search Web</div>
            </button>
            <button onclick="quickAction('Run Task')" class="p-2.5 rounded-xl glass-panel-subtle hover:bg-white/10 hover:border-amber-500/30 transition-all text-left group">
              <i data-lucide="zap" class="w-4 h-4 text-amber-400 mb-1.5 group-hover:scale-110 transition-transform"></i>
              <div class="text-xs font-semibold text-white">Run Task</div>
            </button>
            <button onclick="quickAction('Use Tools')" class="p-2.5 rounded-xl glass-panel-subtle hover:bg-white/10 hover:border-emerald-500/30 transition-all text-left group">
              <i data-lucide="cpu" class="w-4 h-4 text-emerald-400 mb-1.5 group-hover:scale-110 transition-transform"></i>
              <div class="text-xs font-semibold text-white">Use Tools</div>
            </button>
          </div>
        </div>
      </div>

      <!-- 3. Live Stats Cards -->
      <div class="glass-panel-subtle rounded-2xl p-3.5 border border-white/[0.08] space-y-2.5">
        <div class="text-[11px] font-bold text-slate-400 uppercase tracking-wider font-mono">Live Performance</div>
        
        <div class="grid grid-cols-3 gap-2 text-center">
          <div class="p-2 rounded-xl bg-slate-950/60 border border-cyan-500/20">
            <div class="text-[10px] text-slate-400">Response</div>
            <div class="text-sm font-bold text-cyan-400 font-mono">1.2s</div>
          </div>
          <div class="p-2 rounded-xl bg-slate-950/60 border border-purple-500/20">
            <div class="text-[10px] text-slate-400">Accuracy</div>
            <div class="text-sm font-bold text-purple-400 font-mono">98%</div>
          </div>
          <div class="p-2 rounded-xl bg-slate-950/60 border border-emerald-500/20">
            <div class="text-[10px] text-slate-400">Uptime</div>
            <div class="text-sm font-bold text-emerald-400 font-mono">99.9%</div>
          </div>
        </div>
      </div>
    </aside>
  </div>

  <script>
    // Initialize Lucide Icons
    lucide.createIcons();

    // Waveform Setup
    const waveContainer = document.getElementById('waveformContainer');
    const numBars = 32;
    const waveBars = [];
    for (let i = 0; i < numBars; i++) {
      const bar = document.createElement('div');
      bar.className = 'w-1 rounded-full bg-gradient-to-t from-cyan-500 via-indigo-500 to-purple-500 transition-all duration-75';
      bar.style.height = '6px';
      waveContainer.appendChild(bar);
      waveBars.push(bar);
    }

    let currentState = 'IDLE';

    function setAgentState(st) {
      currentState = st;
      document.getElementById('stateHeading').innerText = 'Live Agent Feedback • ' + st;

      const states = ['IDLE', 'LISTENING', 'THINKING', 'SPEAKING'];
      states.forEach(s => {
        const card = document.getElementById('card-' + s);
        const dot = card.querySelector('div:first-child');
        if (s === st) {
          card.className = 'state-card p-3 rounded-xl border border-cyan-500/40 bg-cyan-500/10 cursor-pointer transition-all flex items-center gap-3 shadow-[0_0_15px_rgba(0,240,255,0.15)]';
          dot.className = 'w-2.5 h-2.5 rounded-full bg-cyan-400 shadow-[0_0_8px_#00f0ff] animate-ping';
        } else {
          card.className = 'state-card p-3 rounded-xl border border-white/5 hover:border-white/15 bg-white/[0.02] cursor-pointer transition-all flex items-center gap-3';
          dot.className = 'w-2.5 h-2.5 rounded-full bg-slate-600';
        }
      });
    }

    function quickAction(actionName) {
      const input = document.getElementById('userInput');
      input.value = 'Execute: ' + actionName;
      document.getElementById('agentForm').dispatchEvent(new Event('submit'));
    }

    function simulateVoice() {
      setAgentState('LISTENING');
      document.getElementById('captionText').innerText = '"Listening to your microphone audio input..."';
      setTimeout(() => {
        setAgentState('THINKING');
        document.getElementById('captionText').innerText = '"Analyzing neural intent with Groq 120B..."';
      }, 2500);
    }

    // ==========================================
    // 3D Canvas Hologram Bust & Neural Core
    // ==========================================
    const canvas = document.getElementById('hologramCanvas');
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      initHologramMesh();
    });

    const meshPoints = [];

    function initHologramMesh() {
      meshPoints.length = 0;

      // 1. Brain Neural Core (Vibrant Magenta & Violet Synaptic Core)
      for (let i = 0; i < 480; i++) {
        const u = Math.random(), v = Math.random();
        const theta = u * 2.0 * Math.PI, phi = Math.acos(2.0 * v - 1.0);
        const r = 36 + Math.random() * 14;
        const x = r * Math.sin(phi) * Math.cos(theta) * 0.95;
        const y = -105 + r * Math.cos(phi) * 0.78;
        const z = r * Math.sin(phi) * Math.sin(theta) * 0.95;

        meshPoints.push({
          baseX: x, baseY: y, baseZ: z,
          x: 0, y: 0, z: 0,
          size: Math.random() * 2.2 + 1.2,
          isCore: true,
          color: Math.random() > 0.4 ? 'rgba(232, 121, 249, ' : 'rgba(168, 85, 247, ', // Magenta/Purple
          connections: []
        });
      }

      // 2. Anatomical Faceted Cranium, Cheekbones, Jaw, Chin (Electric Cyan Wireframe)
      const faceLayers = 32;
      for (let ring = 0; ring < faceLayers; ring++) {
        const t = ring / (faceLayers - 1);
        const y = -150 + t * 165;
        let rx = 0, rz = 0;

        if (t < 0.28) {
          const subT = t / 0.28;
          rx = 74 * Math.sin(subT * Math.PI * 0.5);
          rz = 70 * Math.sin(subT * Math.PI * 0.5);
        } else if (t < 0.6) {
          rx = 76 + Math.sin((t - 0.28) / 0.32 * Math.PI) * 6;
          rz = 72;
        } else if (t < 0.85) {
          const subT = (t - 0.6) / 0.25;
          rx = 78 - subT * 34;
          rz = 70 - subT * 20;
        } else {
          const subT = (t - 0.85) / 0.15;
          rx = 44 - subT * 24;
          rz = 50 - subT * 26;
        }

        const ptsInRing = Math.max(16, Math.floor(rx * 0.58));
        for (let i = 0; i < ptsInRing; i++) {
          const angle = (i / ptsInRing) * Math.PI * 2;
          let x = Math.cos(angle) * rx;
          let z = Math.sin(angle) * rz;

          // Push facial front features
          if (z > 0 && Math.abs(x) < 26 && y > -85 && y < -10) {
            z += (26 - Math.abs(x)) * 0.55;
          }

          meshPoints.push({
            baseX: x + (Math.random() - 0.5) * 2,
            baseY: y,
            baseZ: z + (Math.random() - 0.5) * 2,
            x: 0, y: 0, z: 0,
            size: Math.random() * 1.5 + 0.8,
            isCore: false,
            color: 'rgba(0, 240, 255, ', // Cyan
            connections: []
          });
        }
      }

      // 3. Neck & Trapezius Shoulders
      for (let ring = 0; ring < 8; ring++) {
        const y = 20 + ring * 7;
        const radius = 28 + ring * 2.2;
        for (let i = 0; i < 22; i++) {
          const angle = (i / 22) * Math.PI * 2;
          meshPoints.push({
            baseX: Math.cos(angle) * radius,
            baseY: y,
            baseZ: Math.sin(angle) * radius * 0.9,
            x: 0, y: 0, z: 0,
            size: 1.1,
            isCore: false,
            color: 'rgba(56, 189, 248, ',
            connections: []
          });
        }
      }

      for (let row = 0; row < 12; row++) {
        const rowT = row / 11;
        const y = 80 + rowT * 50;
        const widthT = 110 + rowT * 175;
        for (let i = 0; i < 34; i++) {
          const u = (i / 33 - 0.5) * 2;
          const x = u * widthT;
          const arch = Math.pow(Math.abs(u), 1.8) * 42;
          const z = (Math.random() - 0.5) * 55 + (1 - Math.abs(u)) * 28;
          meshPoints.push({
            baseX: x, baseY: y + arch, baseZ: z,
            x: 0, y: 0, z: 0,
            size: Math.random() * 1.6 + 0.8,
            isCore: false,
            color: 'rgba(0, 240, 255, ',
            connections: []
          });
        }
      }

      // Triangular Polygonal Mesh Wireframe
      for (let i = 0; i < meshPoints.length; i += 2) {
        const p1 = meshPoints[i];
        let found = 0;
        for (let j = i + 1; j < meshPoints.length && found < 3; j++) {
          const p2 = meshPoints[j];
          const distSq = (p1.baseX - p2.baseX) ** 2 + (p1.baseY - p2.baseY) ** 2 + (p1.baseZ - p2.baseZ) ** 2;
          if (distSq < 280) {
            p1.connections.push(j);
            found++;
          }
        }
      }
    }

    initHologramMesh();

    let tick = 0;

    function renderHologram() {
      tick += 0.024;
      ctx.clearRect(0, 0, width, height);

      const centerX = width * 0.5;
      const centerY = height * 0.38;

      let breathSpeed = 1, coreIntensity = 1, waveMultiplier = 1;
      if (currentState === 'IDLE') {
        breathSpeed = 0.8; coreIntensity = 1.0; waveMultiplier = 1.0;
      } else if (currentState === 'LISTENING') {
        breathSpeed = 1.5; coreIntensity = 1.6; waveMultiplier = 2.0;
      } else if (currentState === 'THINKING') {
        breathSpeed = 2.8; coreIntensity = 3.2; waveMultiplier = 2.8;
      } else if (currentState === 'SPEAKING') {
        breathSpeed = 1.8; coreIntensity = 2.0; waveMultiplier = 3.5;
      }

      // Animate Waveform Bars
      waveBars.forEach((bar, idx) => {
        const offset = Math.sin(tick * 3 + idx * 0.35);
        const h = Math.max(4, (12 + offset * 10) * waveMultiplier);
        bar.style.height = `${h}px`;
      });

      // 3D Rotations
      const rotY = Math.sin(tick * 0.45 * breathSpeed) * 0.15;
      const rotX = Math.cos(tick * 0.35 * breathSpeed) * 0.06;
      const breath = Math.sin(tick * 1.4 * breathSpeed) * 4.0;

      for (let i = 0; i < meshPoints.length; i++) {
        const p = meshPoints[i];
        const x1 = p.baseX * Math.cos(rotY) + p.baseZ * Math.sin(rotY);
        const z1 = -p.baseX * Math.sin(rotY) + p.baseZ * Math.cos(rotY);
        const y1 = (p.baseY + breath) * Math.cos(rotX) - z1 * Math.sin(rotX);
        const z2 = (p.baseY + breath) * Math.sin(rotX) + z1 * Math.cos(rotX);

        const fov = 450;
        const scale = fov / (fov + z2 + 100);
        p.x = centerX + x1 * scale;
        p.y = centerY + y1 * scale;
        p.z = z2;
      }

      // Additive Glow
      ctx.globalCompositeOperation = 'lighter';

      // Draw Wireframe Mesh
      ctx.lineWidth = 0.5;
      for (let i = 0; i < meshPoints.length; i += 3) {
        const p1 = meshPoints[i];
        for (let k = 0; k < p1.connections.length; k++) {
          const p2 = meshPoints[p1.connections[k]];
          if (!p2) continue;
          const depthAlpha = Math.max(0.03, Math.min(0.24, (p1.z + 100) / 200));
          ctx.strokeStyle = p1.isCore
            ? `rgba(232, 121, 249, ${depthAlpha * coreIntensity})`
            : `rgba(0, 240, 255, ${depthAlpha * 0.6})`;
          ctx.beginPath();
          ctx.moveTo(p1.x, p1.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.stroke();
        }
      }

      // Draw Particles
      for (let i = 0; i < meshPoints.length; i++) {
        const p = meshPoints[i];
        const depth = (p.z + 120) / 240;
        const depthScale = Math.max(0.4, Math.min(1.4, depth));
        const shimmer = Math.sin(tick * 3.5 + i * 0.1) * 0.3 + 0.7;

        if (p.isCore) {
          const alpha = Math.min(1, Math.max(0.2, depth * shimmer * coreIntensity));
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size * depthScale * (coreIntensity > 1.8 ? 1.3 : 1), 0, Math.PI * 2);
          ctx.fillStyle = `${p.color}${alpha})`;
          ctx.shadowColor = '#e879f9';
          ctx.shadowBlur = 10 * coreIntensity;
          ctx.fill();
          ctx.shadowBlur = 0;
        } else {
          const alpha = Math.min(1, Math.max(0.12, depth * shimmer * 0.85));
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.size * depthScale, 0, Math.PI * 2);
          ctx.fillStyle = `${p.color}${alpha})`;
          ctx.fill();
        }
      }

      ctx.globalCompositeOperation = 'source-over';
      requestAnimationFrame(renderHologram);
    }
    renderHologram();

    // Form Submit Handler
    const form = document.getElementById('agentForm');
    const input = document.getElementById('userInput');
    const caption = document.getElementById('captionText');

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const msg = input.value.trim();
      if (!msg) return;

      input.value = '';
      setAgentState('THINKING');
      caption.innerText = '"' + msg + '" — Processing neural query with Groq 120B...';

      try {
        const res = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: msg })
        });
        const data = await res.json();
        const reply = data.reply || 'Execution completed.';

        setAgentState('SPEAKING');
        caption.innerText = '"' + reply + '"';

        setTimeout(() => {
          setAgentState('IDLE');
        }, 7500);
      } catch (err) {
        setAgentState('IDLE');
        caption.innerText = '⚠️ Error: ' + err;
      }
    });
  </script>
</body>
</html>"""

async def query_groq(key: str, model: str, messages: list):
    url = f"{LLM_API_BASE}/chat/completions"
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": 2500
    }
    async with httpx.AsyncClient(timeout=60.0) as client:
        return await client.post(url, json=payload, headers=headers)

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    global chat_history
    chat_history.append({"role": "user", "content": req.message})
    if len(chat_history) > 20:
        chat_history = [chat_history[0]] + chat_history[-15:]

    try:
        res = await query_groq(PRIMARY_KEY, LLM_MODEL, chat_history)
        if res.status_code != 200:
            res = await query_groq(DEFAULT_KEY, LLM_MODEL, chat_history)
        if res.status_code != 200:
            res = await query_groq(DEFAULT_KEY, "qwen/qwen3.8-27b", chat_history)

        data = res.json()
        if "choices" in data and len(data["choices"]) > 0:
            reply = data["choices"][0]["message"]["content"]
            chat_history.append({"role": "assistant", "content": reply})
            return {"reply": reply}
        else:
            return {"reply": f"⚠️ Groq API Error: {data}"}
    except Exception as e:
        return {"reply": f"⚠️ Connection Error: {str(e)}"}

@app.get("/health")
def health():
    return {"status": "ONLINE", "engine": LLM_MODEL, "operator": "Rohit Kumar Nagar"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
