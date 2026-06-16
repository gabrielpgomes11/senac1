const nodemailer = require('nodemailer');

async function enviarEmailRedefinicao(emailUsuario, nomeUsuario, tokenSeguranca) {
  // Configuração do servidor de disparo (SMTP)
  const transporter = nodemailer.createTransport({
    host: "://seu-provedor.com",
    port: 587,
    secure: false, // true para porta 465, false para outras
    auth: {
      user: "seu_usuario_smtp",
      pass: "sua_senha_smtp",
    },
  });

  // URL do seu sistema que receberá o token para trocar a senha
  const linkRedefinicao = `https://seusite.com{tokenSeguranca}`;

  // Definição da mensagem
  const info = await transporter.sendMail({
    from: '"Suporte Seu Sistema" <suporte@seusite.com>',
    to: emailUsuario,
    subject: "🔐 Redefinição de Senha",
    // Versão em texto puro (caso o leitor de e-mail do usuário bloqueie HTML)
    text: `Olá, ${nomeUsuario}. Acesse este link para redefinir sua senha: ${linkRedefinicao}`,
    // Versão HTML bem estruturada e estilizada inline
    html: `
      <div style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px; max-width: 600px; margin: 0 auto; border: 1px solid #e0e0e0; border-radius: 8px;">
        <h2 style="color: #333333; text-align: center;">Recuperação de Conta</h2>
        <p style="color: #555555; font-size: 16px; line-height: 1.5;">Olá, <strong>${nomeUsuario}</strong>,</p>
        <p style="color: #555555; font-size: 16px; line-height: 1.5;">Recebemos uma solicitação para redefinir a senha da sua conta. Se você não fez essa solicitação, basta ignorar este e-mail.</p>
        
        <div style="text-align: center; margin: 30px 0;">
          <a href="${linkRedefinicao}" target="_blank" style="background-color: #007bff; color: #ffffff; padding: 14px 24px; text-decoration: none; font-size: 16px; font-weight: bold; border-radius: 5px; display: inline-block;">Redefinir Minha Senha</a>
        </div>
        
        <p style="color: #999999; font-size: 12px; text-align: center;">Este link é válido por 1 hora. Por segurança, não compartilhe este e-mail com ninguém.</p>
        <hr style="border: 0; border-top: 1px solid #e0e0e0; margin: 20px 0;">
        <p style="color: #999999; font-size: 12px; text-align: center;">© 2026 Seu Sistema. Todos os direitos reservados.</p>
      </div>
    `,
  });

  console.log("E-mail enviado com sucesso: %s", info.messageId);
}