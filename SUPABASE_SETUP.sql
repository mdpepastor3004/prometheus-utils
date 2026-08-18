-- Supabase SQL Editor에서 실행할 SQL
-- 1) leads 테이블 생성
CREATE TABLE IF NOT EXISTS leads (
  id BIGSERIAL PRIMARY KEY,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT NOT NULL,
  source TEXT DEFAULT '',
  score TEXT DEFAULT '',
  device TEXT DEFAULT '',
  page TEXT DEFAULT ''
);

-- 2) RLS 활성화
ALTER TABLE leads ENABLE ROW LEVEL SECURITY;

-- 3) 누구나 INSERT 가능 (익명 사용자용)
DROP POLICY IF EXISTS "anon_insert" ON leads;
CREATE POLICY "anon_insert"
  ON leads
  FOR INSERT
  TO anon
  WITH CHECK (true);

-- 4) service_role은 SELECT/UPDATE/DELETE 가능
DROP POLICY IF EXISTS "service_all" ON leads;
CREATE POLICY "service_all"
  ON leads
  FOR ALL
  TO service_role
  USING (true)
  WITH CHECK (true);

-- 5) 인덱스
CREATE INDEX IF NOT EXISTS idx_leads_created_at ON leads(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_leads_source ON leads(source);
CREATE INDEX IF NOT EXISTS idx_leads_email ON leads(email);
